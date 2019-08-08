# Author:Peng Chen
import getpass

username=input("username:")
# password =input("passwoed:")
password = getpass.getpass("password")
print(username,password)