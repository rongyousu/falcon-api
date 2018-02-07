from annoy import AnnoyIndex
import datetime


starttime = datetime.datetime.now()
print starttime

f=4096
t = AnnoyIndex(f,metric='euclidean')  # Length of item vector that will be indexed

file = open("./data/imgs.txt","r")  


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
    #print v
    t.add_item(int(itemid), v)

t.build(20) # 10 trees
t.save('./data/loadimg.ann')


endtime = datetime.datetime.now()
print (endtime - starttime).seconds

uu = AnnoyIndex(f,metric='euclidean')

uu.load('./data/loadimg.ann')

print(uu.get_nns_by_item(53952,10,search_k=-1, include_distances=True))
