# _*_coding:utf-8 _*_
# CREATE BY  :cp
# CREATE TIME:2019/8/11 18:18
# FILE       :dictionary.PY
# IDE        :PyCharm

info ={
    'syu1101':"TengLan Wu",
    'syu1102':"LongZe Luola",
    'syu1103':"XiaoZe Maliya",
}
b ={
    'syu1101':"AAAA",
    1:2,
    2:5,
}
print(info)
# 获取字典值
print(info["syu1101"])
print(info.get("syu1103"))
# 合并两字典 相同key覆盖 不同则追加
info.update(b)
print(info)
dict_item = info.items()
print(dict_item)
print(dict.fromkeys([1,2,4],["1",2,{"3":"3"}]))

for i in info:
    print(i,info[i])
