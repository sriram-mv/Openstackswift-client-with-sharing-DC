# >>> import json
# >>> url = 'https://api.github.com/some/endpoint'
# >>> payload = {'some': 'data'}
# >>> headers = {'content-type': 'application/json'}

# >>> r = requests.post(url, data=json.dumps(payload), headers=headers)
# from requests.auth import AuthBase
import requests
import io
# class PizzaAuth(AuthBase):
#     """Attaches HTTP Pizza Authentication to the given Request object."""
#     def __init__(self, username):
#         # setup any auth-related data here
#         self.username = username

#     def __call__(self, r):
#         # modify and return the request
#         r.headers['X-Pizza'] = self.username
#         return r
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
		
		print "Downloading"
		headers={"X-Auth-Token":tester.xauthtoken}
		r=requests.get(url12,headers=headers)
		#print r.headers

		# print len(r.content)
		file_name = url12.split('/')[-1]
		if ".png" in file_name:
			fh=open(file_name,'ab+')
	# fh=open(file_name,'rb')
			fh.write(r.content)
			fh.close()
		print "Downloaded!"

	else:
		print "Error Occured"
		exit(1)
	# url12='http://127.0.0.1:8080/v1/AUTH_test/images/dropbox.png'
	

if __name__ == '__main__':
	main()