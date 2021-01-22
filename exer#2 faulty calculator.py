print("enter the operator")
op= input()
print("enter two numbers:")
num1= int(input())
num2= int(input())



if op == '+':
    if num1==56 and num2==9:
        print("the result is 77")
    else:
        print("the result is", (num1+num2))
elif op == '-':
    print("the result is", (num1-num2))
elif op == '*':
    if num1==45 and num2==3:
        print("the result is 555")
    else:
        print("the result is", (num1*num2))
elif op == '/':
    if num1==56 and num2==6:
        print("the result is 4")
    else:
        print("the result is", (num1/num2))
else:
        print("enter the correct values")
