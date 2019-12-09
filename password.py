import getpass

#该函数不会弹出用户名的输入提示。 它会根据该用户的shell环境或者会依据本地系统的密码库（支持 pwd 模块的平台）来使用当前用户的登录名
user = getpass.getuser()
passwd = getpass.getpass()


def svc_login(user, passwd):
    if user == 'root' and passwd == 'test1234':
        return True
    else:
        return False

if svc_login(user, passwd):
    print("Yay!")
else:
    print("Boo!")