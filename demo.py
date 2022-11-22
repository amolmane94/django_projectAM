import os
import socket

ip=socket.gethostbyname('www.google.com')
print(ip)

'''
try:
    filename='/mnt/demo.py'
    f=open(filename,'r')
    text=f.read()
    print(text)
    f.close()
except IOError:
    print("problem reading",+filename)


'''
os.name.__doc__
'''
out = os.path.isfile('/mnt/demo1.py')
if out==True:
    print("File present at ",os.getcwd())
else:
    print("file not present")

'''
#print(out)
#print("Hello World!!!!")
#print("current working directory::",os.getcwd())
#os.chdir('../')
#print("after ../",os.getcwd())
#print('os name',os.name)

#s.mkdir("/mnt/myproject")
#os.rmdir('/mnt/myproject')
#print(os.listdir("/mnt"))

