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

def Adminornot():
	f=open('/etc/swift/proxy-server.conf','r')
	user="user"
	admin =".admin"
	Adminornotdict={}
	userlist=list()
	adminlist=list()
	f1=0
	i=iter(userlist)
	j=iter(adminlist)
	length=0
	for line in f:
		if user in line:
			f1=f1+1
		if f1>2:
			if user in line:
				newone=line.split('=')
				# print newone
			# newone3=newone[1].split('.')
				newone2=newone[0].split('_')
				# print newone2
				userlist.append(newone2[1]+":"+newone2[2])	
			# passwords=newone3[0].split('\n')
				if admin in line:
					adminlist.append('1')
				else:
					adminlist.append('0')	
					# print 'User:',newone2[1],'Password:',
	# print userlist
	# print passlist
	while length < len(userlist):
		length= length + 1
		Adminornotdict[i.next()]=j.next()
	length=0
	k=iter(userlist)
	while length < len(userlist):
			length=length+1
			ensure_dir(os.getcwd()+'/'+k.next())
	return Adminornotdict
def getuserlist():
	f=open('/etc/swift/proxy-server.conf','r')
	user="user"
	admin ="admin"
	Authdict={}
	userlist=list()
	passlist=list()
	f1=0
	i=iter(userlist)
	j=iter(passlist)
	length=0
	for line in f:
			if user in line:
				# if admin in line:

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
		# print 'User:',i.next()," Password:",j.next()
	length=0
	k=iter(userlist)
	while length < len(userlist):
			length=length+1
			ensure_dir(os.getcwd()+'/'+k.next())	
	
	return EntireAuth(userlist,passlist)
	
def main():
	print getuserlist()
	print Adminornot()
if __name__ == '__main__':
	main()
