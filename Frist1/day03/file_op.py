# _*_coding:utf-8 _*_
# CREATE BY  :cp
# CREATE TIME:2019/8/13 22:39
# FILE       :file_op.PY
# IDE        :PyCharm

f = open("yesteday",'r',encoding='utf-8')# 就是文件的句柄
print(f.readlines())

for line in f:
    print(line)