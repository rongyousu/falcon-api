#coding: utf-8

import os
import sys
import MySQLdb
import datetime
import requests
import cv2
import numpy as np
import time

# 下载图片
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)


def get_img_vector(path):
       #print path
       img=cv2.imread(path)
       gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       #print gray
       new_img=cv2.resize(gray,dsize=(64,64))
       img_mean=cv2.mean(new_img)

       return new_img > img_mean[0]


def get_to_text(img_vector):
       #print img_vector
       sample=img_vector.reshape((1,4096))
       b=np.array(sample)
       b=b.astype(np.float)
       arrays=str(b.tolist())
       arrays=arrays.replace('[[','').replace(']]','')
       return arrays
       



if __name__ == '__main__':


	today = datetime.datetime.now()
        yesterday=today + datetime.timedelta(days=-1)
        todayf=yesterday.strftime('%Y-%m-%d')
        args = sys.argv
        print len(args)
        if len(args)>1:
              dt = args[2]
              theday=time.strptime(dt,'%Y%m%d')
              todayf=time.strftime('%Y-%m-%d',theday)
        
        print todayf
        
        starttime = str(todayf) + ' 00:00:00'
        endtime = str(todayf) + ' 23:59:59'

        starttime='2017-05-15 21:00:00'          

        try:
              connection = MySQLdb.connect(user='xes_datamining',passwd='m99gESobIArSCCpMoigyrqPOwZAGkDze',host='10.10.6.205',db='crm',charset='utf8',port=3306)
        except:
              print "Could not connect to MySQL server."
              exit(0)
        cursor = connection.cursor()
        sql="select id, recommend_answer from xes_crm_questions  where  status in (3,4,5)   and is_ref=0   and  recommend_answer  is not null  and  length(recommend_answer)>0  and ctime_format>='"+str(starttime)+"' and ctime_format <='"+str(endtime)+"'  "

        cursor.execute(sql)
        rows = cursor.fetchall()
        print len(rows)
        if not rows:
             sys.exit(0)
        exit(0)
        
        ppath='/data/falcon/offline/pic_sim/'
        f=file(ppath+'data/imgs.txt','a+')

        tmp_path=ppath+'data/pic_files_tmp/'
        if os.path.exists(tmp_path):
               shutil.rmtree(tmp_path)

        os.makedirs(tmp_path)


        for r in rows:
               imgurl=str(r[1])
               id=str(r[0])
               filepath = tmp_path+id+'.png'
               #print filepath
               dowloadPic(imgurl,filepath)
               if os.path.exists(filepath):
                      img_vector = get_img_vector(filepath)
                      array_str = get_to_text(img_vector)
              
                      f.write( array_str +'@'+str(id)+'\n')
                      f.flush()
        f.close()
        if cursor !=None:
               cursor.close()
        if connection !=None:
               connection.close()
