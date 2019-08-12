# _*_coding:utf-8 _*_
# CREATE BY  :cp
# CREATE TIME:2019/8/12 22:01
# FILE       :set.PY
# IDE        :PyCharm
# 集合也是无序的
lsit_1 = [1, 2, 3, 5, 5, 6, 7, 8, 9]
list_1 = set(lsit_1)
list_2 = set([12, 324, 5, 5, 6, 7568, 89, 67, ])
print(list_1, type(list_1))

# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集
print(list_1.union(list_2))
print(list_1 | list_2)
# 差集
print(list_1.difference(list_2))
print(list_1 - list_2)
list_3 = set([1, 2, 5])
# 子集
print(list_3.issubset(list_1))
# 父集
print(list_1.issuperset(list_3))

# 对称差集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
