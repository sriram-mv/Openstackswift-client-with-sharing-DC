import sys
import io
import os
def ensure_dir(f):
	if not os.path.exists(f):
		try:
			os.makedirs(f)
		except OSError as exception:
			if exception.errno != 17:
				raise
def EntireAuth(userlist,passlist):
	userIterator=iter(userlist)
	passIterator=iter(passlist)
	length=0
	Authdict={}
	while length < len(userlist):
		length=length+1
		Authdict[userIterator.next()]=passIterator.next()
	return Authdict

def main():
	f=open('/home/sriram/Openstack Project/testopenstackproxy.txt','r')
	user="user"
	Authdict={}
	userlist=list()
	passlist=list()
	f1=0
	i=iter(userlist)
	j=iter(passlist)
	length=0
	for line in f:
			if user in line:
				f1=f1+1
				if f1>2:
					newone=line.split('=')
					newone3=newone[1].split('.')
					newone2=newone[0].split('_')
					passwords=newone3[0].split('\n')
					passlist.append(passwords[0])
					userlist.append(newone2[1]+":"+newone2[2])
					# print 'User:',newone2[1],'Password:',
	# print userlist
	# print passlist
	while length < len(userlist):
		length= length + 1
		print 'User:',i.next()," Password:",j.next()
	length=0
	k=iter(userlist)
	while length < len(userlist):
			length=length+1
			ensure_dir(os.getcwd()+'/'+k.next())	
	
	print EntireAuth(userlist,passlist)
if __name__ == '__main__':
	main()
