num = int(input("Enter the number of rows of the stars:"))

binary = int(input("Enter 0 or 1:"))
i=0
j=1
if binary:
    bool_val = True
    print(bool_val)
    
    for i in range(0,num):
        for j in range(1,i+1):
            print("*",end="")
        print("*")

        
else:
    bool_val = False
    print(bool_val)

    for i in range(num-1,-1,-1):
        for j in range(1,i+1):
            print("*",end="")
        print("*")
        
 