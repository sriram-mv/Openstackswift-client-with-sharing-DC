import io,sys,os
from collections import defaultdict
import requests
from copy import deepcopy
def ensure_dir(f):
	if not os.path.exists(f):
		try:
			os.makedirs(f)
		except OSError as exception:
			if exception.errno != 17:
				raise
class User():
	def __init__(self, xauthtoken,xstoragetoken):
		# super(User, self).__init__()
		self.xauthtoken = xauthtoken
		self.xstoragetoken = xstoragetoken
# class CopiableSetDict(SetDict):
#     def __copy__(self):
#         # Create an uninitialized instance
#         other = self.__class__.__new__(self.__class__)
#         # Give it the same attributes (references)
#         other.__dict__ = self.__dict__.copy()
#         # Create a copy of d dict so other can have its own
#         other.d = self.d.copy()
#         return other
def StatusatClient():
	Container = defaultdict(list)
	alldirsobjects=list()
	length=0
	# Container={}
	for dirname, dirnames, filenames in os.walk(os.getcwd()+'/'+sys.argv[1]+'/'):
	# print path to all subdirectories first.
		# for subdirname in dirnames:
		# 	alldirsobjects.append(os.path.join(dirname,subdirname))
	# print path to all filenames.
		for filename in filenames:
			alldirsobjects.append(os.path.join(dirname,filename))
	Iterator=iter(alldirsobjects)
	while length < len(alldirsobjects):
		itsme=Iterator.next()
		# print itsme.split('/')[-1]
		Container[itsme.split('/')[-2]].append(itsme.split('/')[-1])
		# print itsme.split('/')[-1]
		length=length+1
	return Container

def StatusatServer():
	FinalSyncList=defaultdict(list)
	url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
	head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
	r=requests.get(url,headers=head)
	url12=sys.argv[3]
	auth="AUTH"
	tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
	# print tester.xauthtoken,tester.xstoragetoken
	test=tester.xauthtoken
	# print test
	if test == None:
		print "Wrong username or password"
		exit(1)
	if auth in test:
		# IntialPath=os.getcwd()
		# print "Showing Containers!"
		headers={"X-Auth-Token":tester.xauthtoken}
		r=requests.get(url12,headers=headers)
		# print r.content
		Containerlist=r.content.split('\n')
		# print Containerlist
		size=len(Containerlist)-1
		ContainerIter=iter(Containerlist)
		# while size>0:
		# 	ensure_dir(os.getcwd()+'/'+sys.argv[1]+'/'+ContainerIter.next()+'/')

		# 	size=size-1
		Containersize=len(Containerlist)-1
		ContainerIter=iter(Containerlist)
		Objectsize=0
		while Containersize>0:
			container=ContainerIter.next()			
			r=requests.get(url12+'/'+container+'/',headers=headers)
			# print 'Objects inside ',container
			Objectlist=r.content.split('\n')

			
			# print Objectlist
			Objectsize=len(Objectlist)-1

			ObjectIter=iter(Objectlist)

			while Objectsize>0:
				Object=ObjectIter.next()
				# print url12
				# print container
				# print Object
				FinalSyncList[container].append(Object)
				# print os.getcwd()
				# q=requests.get(url12+'/'+container+'/'+Object,headers=headers)
				# fh=open(os.getcwd()+'/'+sys.argv[1]+'/'+container+'/'+Object,'wb+')
				# # fh=open(file_name,'rb')
				# fh.write(q.content)
				# fh.close()
				# print os.getcwd()
				# print q.content
				# if container in os.getcwd()
				# os.chdir(os.getcwd()+'/'+sys.argv[1]+'/'+container+'/')
				# print os.getcwd()	
				Objectsize=Objectsize-1
			# os.chdir("../")
			Containersize=Containersize-1
	return FinalSyncList

def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)

def inClientorServer(serverList,clientList,differenceList):
	length=0
	Filesynclist=list()
	differenceListIter=iter(differenceList)
	while length<len(differenceList):
		check=differenceListIter.next()
		length=length+1
		if check in clientList:
			Filesynclist.append(check)
			print check,"is a new file in clientList"

		if check in serverList:
			# print check,"is a new file in serverList"
			print "Line 131"
	return Filesynclist

def inServerorClient(serverList,clientList,differenceList):
	length=0
	Filesynclist=list()
	differenceListIter=iter(differenceList)
	while length<len(differenceList):
		check=differenceListIter.next()
		length=length+1
		if check in clientList:
			print check,"is a new file in clientList"

		if check in serverList:
			print check,"is a new file in serverList"
			Filesynclist.append(check)
	return Filesynclist

def UncorrectPathtoCorrectpath():
	quench=list()
	fixer=os.getcwd()
	quench=fixer.split(" ")
	# print quench
	correctpath=quench[0]+'\ '+quench[1]
	return correctpath

def putobjects(DicttobeSynced):
	if(len(DicttobeSynced)==0):
		return
	url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
	head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
	r=requests.get(url,headers=head)
	url12=sys.argv[3]
	auth="AUTH"
	# print r.headers
	tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
	# print tester.xauthtoken,tester.xstoragetoken
	test=tester.xauthtoken
	# print test
	if test == None:
		print "Wrong username or password"
		exit(1)
	if auth in test:
		print "Uploadiing"
		print os.getcwd()
			
		#print r.headers
		# print len(r.content)
		for key in DicttobeSynced:
			# print key," ",DicttobeSynced[key]
			file_name = key
			value=DicttobeSynced[key]
			newurl=sys.argv[3]+'/'+value+'/'+file_name
			print newurl
			print UncorrectPathtoCorrectpath()+'/'+sys.argv[1]+'/'+value+'/'+file_name
			xmlfile = open(os.getcwd()+'/'+sys.argv[1]+'/'+value+'/'+file_name, 'rb+')
			# r = requests.put(url, data=xmlfile, headers=headers, auth=HTTPDigestAuth("*", "*")
			headers={"X-Auth-Token":tester.xauthtoken}
			r=requests.put(newurl,headers=headers,data=xmlfile)
			# print r.content
		print "Uploaded!"

	else:
		print "Error Occured"
		exit(1)
def getobjects(DicttobeSynced):
	if(len(DicttobeSynced)==0):
		return
	url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
	head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
	r=requests.get(url,headers=head)
	url12=sys.argv[3]
	auth="AUTH"
	# print r.headers
	tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
	# print tester.xauthtoken,tester.xstoragetoken
	test=tester.xauthtoken
	# print test
	if test == None:
		print "Wrong username or password"
		exit(1)
	if auth in test:
		print "Downloading!"
		for key in DicttobeSynced:
		# print key," ",DicttobeSynced[key]
			file_name = key
			value=DicttobeSynced[key]
			newurl=sys.argv[3]+'/'+value+'/'+file_name
			print newurl
		#	print UncorrectPathtoCorrectpath()+'/'+sys.argv[1]+'/'+value+'/'+file_name
			xmlfile = open(os.getcwd()+'/'+sys.argv[1]+'/'+value+'/'+file_name, 'wb+')
			# r = requests.put(url, data=xmlfile, headers=headers, auth=HTTPDigestAuth("*", "*")
			headers={"X-Auth-Token":tester.xauthtoken}
			r=requests.get(newurl,headers=headers)
			xmlfile.write(r.content)
			xmlfile.close()
		print "Downloaded!"
	else:
		print "Error Occured"
		exit(1)
def buildContainertofileinServer(ServerFiles):
	i=-1
	FiletoContainerdict = {}
	for top in ServerFiles.values(): 
		i=i+1
		key=ServerFiles.keys()[i] 
		for inner in top: 
			FiletoContainerdict[inner]=key
	return FiletoContainerdict	
def buildContainertofileinClient(ClientFiles):
	i=-1
	FiletoContainerdict = {}
	for top in ClientFiles.values(): 
		i=i+1
		key=ClientFiles.keys()[i] 
		for inner in top: 
			FiletoContainerdict[inner]=key
	return FiletoContainerdict
def DictofFileSyncatClient(FileSync,differenceList,Client):
	FileSyncDict={}
	LenFileSync=iter(FileSync)
	length=0
	if(len(FileSync)==0):
		return FileSyncDict
	else:
		while length<len(FileSync):
			check=LenFileSync.next()
			print check
			if Client[check]!="null":
				FileSyncDict[check]=Client[check]
			length=length+1
		return FileSyncDict
def DictofFileSyncatServer(FileSync,differenceList,Server):
	FileSyncDict={}
	LenFileSync=iter(FileSync)
	length=0
	if(len(FileSync)==0):
		return FileSyncDict
	else:
		while length<len(FileSync):
			check=LenFileSync.next()
			print check
			if Server[check]!="null":
				FileSyncDict[check]=Server[check]
			length=length+1
		return FileSyncDict
def FileSyncatClient(ServerFiles,ClientFiles):
	i=0
	while i < len(ClientFiles.values()):
		# differenceList=diff(ServerFiles.values()[0],ClientFiles.values()[0])
		# FileSync=inClientorServer(ServerFiles.values()[0],ClientFiles.values()[0],differenceList)
	
		# Server=buildContainertofileinServer(ServerFiles)
		# Client=buildContainertofileinClient(ClientFiles)

		differenceList=diff(ServerFiles.values()[i],ClientFiles.values()[i])
		FileSync=inClientorServer(ServerFiles.values()[i],ClientFiles.values()[i],differenceList)
	
		# Server=buildContainertofileinServer(ServerFiles)
		Client=buildContainertofileinClient(ClientFiles)
		putobjects((DictofFileSyncatClient(FileSync,differenceList,Client)))
		i=i+1

def FileSyncatServer(ServerFiles,ClientFiles):
	i=0
	while i < len(ServerFiles.values()):
		# differenceList=diff(ServerFiles.values()[0],ClientFiles.values()[0])
		# FileSync=inClientorServer(ServerFiles.values()[0],ClientFiles.values()[0],differenceList)
	
		# Server=buildContainertofileinServer(ServerFiles)
		# Client=buildContainertofileinClient(ClientFiles)

		differenceList=diff(ServerFiles.values()[i],ClientFiles.values()[i])
		FileSync=inServerorClient(ServerFiles.values()[i],ClientFiles.values()[i],differenceList)
	
		Server=buildContainertofileinServer(ServerFiles)
		# Client=buildContainertofileinClient(ClientFiles)
		getobjects((DictofFileSyncatServer(FileSync,differenceList,Server)))
		i=i+1

def Start():
	ServerFiles=defaultdict(list)
	ClientFiles=defaultdict(list)
	FileSync=list()
	ServerFiles=StatusatServer()
	ClientFiles=StatusatClient()
	print "At Server container1 name: ",ServerFiles.keys()[0]
	print "At Server objects in container1: ",ServerFiles.values()[0]
	print "At Server container2 name: ",ServerFiles.keys()[1]
	print "At Server objects in container2 : ",ServerFiles.values()[1]
	print "At Client container1 name: ",ClientFiles.keys()[0]
	print "At Client objects in container1: ",ClientFiles.values()[0]	
	print "At Client container2 name: ",ClientFiles.keys()[1]
	print "At Client objects in container2 : ",ClientFiles.values()[1]
	print "Length at Server: ",len(ServerFiles.values()[0])
	print "Length at Client: ",len(ClientFiles.values()[0])
	print "Total Length of Values at Server",len(ServerFiles.values())
	print "Total Length of Values at Client",len(ClientFiles.values())
	FileSyncatClient(ServerFiles,ClientFiles)
	FileSyncatServer(ServerFiles,ClientFiles)






	# for filename in os.listdir(os.getcwd())
	# print filename
	# os.chdir(os.getcwd())
	# print os.getcwd()
	
if __name__ == '__main__':
	Start()
