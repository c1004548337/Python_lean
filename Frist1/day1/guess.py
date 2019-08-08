# # Author:Peng Chen
age_of_oldbay = 56
# time=0
# while time<3:
#     guess_age = int(input("guess:"))
#     if age_of_oldbay == guess_age:
#         print('''Yes you got id，age is{age}
#         You win！
#         '''.format(age=guess_age))
#         break
#     elif age_of_oldbay<guess_age:
#         print("think bigger!")
#     else:
#         print("think smaller".format(age=guess_age))
#     time+=1
# else:
#     print("you have tried too many times ..fuck off")


for i in range(3):
    guess_age = int(input("guess:"))
    if age_of_oldbay == guess_age:
        print('''Yes you got id，age is{age}
        You win！
        '''.format(age=guess_age))
        break
    elif age_of_oldbay<guess_age:
        print("think bigger!")
    else:
        print("think smaller".format(age=guess_age))
else:
    print("you have tried too many times ..fuck off")

# for i in range(10):
#     print("lopp",i)
