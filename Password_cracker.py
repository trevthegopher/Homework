import hashlib

def hacker(file):
    hashmd5 = input("enter a hash: ")
    count = 1
    pwfile = open(file,"r")
    lines = pwfile.readlines()
    for password in lines:
        password = password.strip()
        filemd5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        print("Attempt number: {} with password: {} ".format(count,password))
        count += 1
    if hashmd5 == filemd5:
        print ("Match found! Password is: {} ".format(password))
hacker("test.txt")

#h = hashlib.md5()
#h.update(b"hello")
#print(h.hexdigest())
#print(hashlib.md5(b"hello").hexdigest())