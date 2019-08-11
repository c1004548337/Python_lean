# _*_coding:utf-8 _*_
# CREATE BY  :cp
# CREATE TIME:2019/8/11 14:54
# FILE       :shopping.PY
# IDE        :PyCharm

product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120)
]
shoppig_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # 类似java的foreach
        # 通过enumerate设置index参数为product_list数据的下标
        for index, item in enumerate(product_list):
            # print(product_list.index(item),item)
            print(index, item)
        user_choice = input("Choice you roduct>>>：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 0 and user_choice < len(product_list):
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shoppig_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is \033[32;1m%s\033[0m" % (p_item, salary))
                else:
                    print("your salary is unenough,your salary:\033[31;1m%s\033[0m" % (salary))
            else:
                print("invalid option")
        elif user_choice == 'q':
            print('------shopping list--------')
            for p in shoppig_list:
                print(p)
            exit("Your current balance:%s"%(salary))
        else:
            print("invalid option")
