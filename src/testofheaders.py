import os,sys,requests
from collections import defaultdict
def test():
	url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
	head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
	r=requests.get(url,headers=head)
	header={}
	listeshes=list()
	header['x-auth-token']=r.headers['x-auth-token']
	q=requests.get(r.headers['x-storage-url'],headers=header)
	# print q.headers
	listeshes=q.content.split()
	Usercontainerreads=defaultdict(list)
	Usercontainerwrites=defaultdict(list)
	length=0
	length1=0
	userlist=list()
	listeshesIter=iter(listeshes)
	while length<len(listeshes):
		z=requests.get(r.headers['x-storage-url']+'/'+listeshesIter.next(),headers=header)
		# print z.content
		
		if z.headers['x-container-read'] != None or z.headers['x-container-write'] != None:
			# print listeshes[length]
			if z.headers['x-container-read']==None:
				pass
			else:	
				userlist=z.headers['x-container-read'].split(',')
				userlistIter=iter(userlist)
				length1=0
				while length1< len(userlist):
					Usercontainerreads[userlistIter.next()].append(listeshes[length])
					length1=length1+1
			if z.headers['x-container-write']==None:
				pass
			else:	
				userlist=z.headers['x-container-write'].split(',')
				userlistIter=iter(userlist)
				length1=0
				while length1< len(userlist):
					Usercontainerwrites[userlistIter.next()].append(listeshes[length])
					length1=length1+1
		length=length+1
	print "x-container-write : ",Usercontainerwrites
	print "x-container-read : ",Usercontainerreads
if __name__ == '__main__':
	test()