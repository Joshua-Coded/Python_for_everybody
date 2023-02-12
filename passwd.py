import getpass


user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):
    print("yah!")

else:
    print("boo!")
