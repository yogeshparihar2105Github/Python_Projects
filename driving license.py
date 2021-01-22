print("enter your age to know you can drive or not")
age = int(input())


if 7 < age < 18:
    print("you can't drive")
elif age==18:
    print("I can't decide whether you can drive or not")
elif 18<age<100:
    print("you can drive")
else:
    print("enter the age between 7 and 100")

