# Author:Peng Chen
count =0
age_of_oldboy=56
while count<3:
    guess_age=int(input("age:"))
    if guess_age==age_of_oldboy:
        print("you got id!")
        break
    elif guess_age<age_of_oldboy:
        print("you think smaller!")
    else:
        print("you think biger!")
    count+=1
    if count==3:
        countine_confirm=input("do you want to keep guessing..?")
        if countine_confirm!="n":
            count=0
else:
    print("game over..!")