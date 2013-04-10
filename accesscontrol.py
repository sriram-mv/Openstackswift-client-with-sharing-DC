# curl -X PUT -i -H "X-Auth-Token: AUTH_tk71d641f0ee6b47a1b4d0fdc11ef7b6f5" -H "X-Container-Read: test:tester3" http://127.0.0.1:8080/v1/AUTH_test/images
import requests
import io
import sys
class User():
	"""docstring for User"""
	def __init__(self, xauthtoken,xstoragetoken):
		# super(User, self).__init__()
		self.xauthtoken = xauthtoken
		self.xstoragetoken = xstoragetoken
def main():

	url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
	head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
	r=requests.get(url,headers=head)
	url12=sys.argv[3]
	container = url12.split('/')[-1]
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
		headers={"X-Container-Read":sys.argv[4],"X-Auth-Token":tester.xauthtoken}
		list1=sys.argv[1].split(":")
		list2=sys.argv[4].split(":")
		if list2[0]==list1[0]:
			r=requests.put(url12,headers=headers)
			print "shared container",container,"with",sys.argv[4]





	else:
		print "Error Occured"
		exit(1)

if __name__ == '__main__':
	main()	