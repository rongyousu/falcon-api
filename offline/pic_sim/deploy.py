# -*- coding: utf-8 -*-
import os
import tarfile
import paramiko
import commands
import urllib
import json
import datetime

from annoy import AnnoyIndex

def make_gzip(f_name):
	current_dir = os.getcwd()
	os.chdir(os.path.dirname(f_name))
	gz_file = '%s.gz' % f_name
	t_file = tarfile.open(gz_file, 'w:gz')
	t_file.add(f_name.split('/')[-1])
	t_file.close()
	os.chdir(current_dir)
	return gz_file

def reload(host):
        result=0
        try:
               url='http://'+str(host)+':8000/api/manager/dbreload/reload_img_tests_annoy_dict?appid=1495158789&appkey=0bea2cb49c1614e5dd8868bd56f9b6cf'
               resp = urllib.urlopen(url)
               content = resp.readline()

               mjson=json.loads(content)
     
               db_nums= int(mjson['db_nums'])
               print 'db_nums:'+str(db_nums)
               if db_nums>0 :
                      result=0
               else:
                      result=1
     
        except Exception as e:
               result=1
               print str(e)
        return  result
       

def rsync_file(f_name, target_list, target_file, r_cmd):
	""" nead ssh-key
	"""
	source_name = make_gzip(f_name)
	failure_list = []
	for target in target_list:
		cmd = 'rsync -avzP %s %s:%s' % (source_name, target, target_file)
		status, output = commands.getstatusoutput(cmd)
                #print target
		if status == 0:     
                        try:
                          
			      cmd_status = remote_cmd(target, r_cmd )
                              print 'cmd_status:'+str(cmd_status)
			      if cmd_status != 0:
			             failure_list.append(target)
                                     continue
                              print 'the remote ' +str(target )+ '  cmd_status:'+ str(cmd_status)
                              
                              result_num = reload (target) 
                              if  result_num != 0:
                                     failure_list.append(target)

                              print  'the ' + str(target) +' reload result_num is :'+ str(result_num ) 
                        except Exception as ee:
                              print str(ee)
                              failure_list.append(target)
		else:
			failure_list.append(target)
	return failure_list

class StatusSSHClient(paramiko.SSHClient):  
	def call(self, command, bufsize=-1):  
		chan = self._transport.open_session()  
		chan.exec_command(command)  
		stdin = chan.makefile('wb', bufsize)  
		stdout = chan.makefile('rb', bufsize)  
		stderr = chan.makefile_stderr('rb', bufsize)  
		status = chan.recv_exit_status()  
		return stdin, stdout, stderr, status 

def remote_cmd(host, cmd):
	ssh_client = StatusSSHClient()
	ssh_client.load_system_host_keys()
	ssh_client.connect(host)
      
	stdin, stdout, stderr, status = ssh_client.call(cmd)
        print stdout.read()
	return status

def send_message(phone,message):
        command = "curl \"http://api.xueersi.com/yunweimsg/sendMsg?phone=" + str(phone) + "&note=" + message + "\" "
        if (os.system(command) == 0):
            print("the message is send success ")
      


def load_model():
        status=0
        try:
             #load model
             f=4096
             model = AnnoyIndex(f,metric='euclidean')        
             file = open("/data/dmpserver/pic_sim/data/imgs.txt","r")
             v=[ 0 for z in xrange(f)]
            
             ISstop=False

             while not ISstop:
                    line = file.readline()
                    if line == None or line =='':
                         ISstop=True
                         break
                    temp=line.strip().split("@")
                    itemid=temp[1]
                    v=temp[0].split(",")
                    v=map(float,v)
                    
                    model.add_item(int(itemid), v)

             model.build(20) # 10 trees
             model.save('/data/dmpserver/pic_sim/data/loadimg.ann')

        except Exception as ee:
             print str(ee)
             status=1     
        return status      

def main():
      
        model_status = load_model()
        failure_list = []
        if model_status ==0:
	          failure_list = rsync_file('/data/dmpserver/pic_sim/data/loadimg.ann', ['10.10.9.251', '10.10.9.252','10.10.9.253','10.10.9.254'], '/data/dmp.xueersi.com/data/img_tests_annoy_dict/loadimg.ann.gz',' cd /data/dmp.xueersi.com/data/img_tests_annoy_dict; tar -xzvf loadimg.ann.gz;  md5sum loadimg.ann > loadimg.ann.md5 ')
	else:
                  failure_list.append('the model is loading error!')

        phones=['18210963058']
        print 'the failure_list:'+str(failure_list)
	if len(failure_list)>0:
               for p in phones:
                     send_message(p, "the api server's model is not success : "+str(failure_list).replace("'","" ).replace(",","" ).replace("[","").replace("]","")  )
		


if __name__ == '__main__':
        today = datetime.datetime.now()

        print datetime.datetime.now()
 	main()
        print datetime.datetime.now()
