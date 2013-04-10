import sys
import io

def main():
	f=open('/home/sriram/Openstack Project/testopenstackproxy.txt','')
	user="user"
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
					f.write(user)
					print line
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
if __name__ == '__main__':
	main()
