import io,sys,os

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def main():
	ensure_dir('/home/sriram/Openstack Project/test1/')
if __name__ == '__main__':
	main()