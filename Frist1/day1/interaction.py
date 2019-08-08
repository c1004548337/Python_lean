# Author:Peng Chen

name = input("name:")
age = int(input("age:"))
print(type(age),type(str(age)))
job = input("job:")

info ='''
----info of %s--------
name:%s
age:%d
job:%s
'''%(name,name,age,job)
# print(info)

info2='''
----info of{name}--------
name:{name}
age:{age}
job:{job}
'''.format(name=name,age=age,job=job)
# print(info2)

info3='''
----info of{0}--------
name:{0}
age:{1}
job:{2}
'''.format(name,age,job)
input(info3)