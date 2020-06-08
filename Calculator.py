print("This Is A Calculator")
print("The Following Task Can Be Done:")
print("--------------------------------")
print("Press 1 For Addition")
print("Press 2 For Substraction")
print("Press 3 For Muliplication")
print("Press 4 For Divison")
print("Press 5 For Calculating Trignometric Ratioes")
print("---------------------------------------------")
print("Please Choose Any")
#Here We are Calling Functions
def statment():
    print("Do You want To Save The result")
    print("Press 1 for Yes")
    print("Press 2 For No")
def call():
    print("Please Enter The Operation To Be Done")
    print("Press 1 For Addition")
    print("Press 2 for Substraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
while(True):
    press=int(input())
    if press==1:
        print("You Have Choosed Addition")
        print("--------------------------")
        a = int(input("Please Enter The First No"))
        b = int(input("Please Enter The Secound No"))
        sum = a + b
        print("The result is",sum)
        print("--------------------------------------")
        statment()
        while(True):
            key=int(input())
            if key==1:
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print(sum)
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print(sum)
                if
