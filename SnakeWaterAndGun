print("                                                                    Welcome to Snake Water And Gun")
print("====================================================================================================================================================================")
name=input("Please Enter Your Name:")
print("Name:",name,"                                                                                                          The no of Chances are:5")
print("========================================================================================================================================================================")
list=["Snake","Water","Gun"]
result=[]
i=0
while(i<5):
    choice=input("Please Enter Choice")
    import random
    a=random.choice(list)
    if a==choice:
        print(choice,"V/s",a)
        print("Draw")
        result.append("Draw")
    if choice=='Snake' and a=='Water':
        print(choice, "V/s", a)
        print("You Won")
        result.append("You Won")
    if choice=='Water' and a=='Snake':
        print("You Loose")
        result.append("You Loose")
        print(choice, "V/s", a)
    if choice=='Snake' and a=='Gun':
        print(choice, "V/s", a)
        print("You Loose")
        result.append("You Loose")
    if choice=='Gun' and a=='Snake':
        print(choice, "V/s", a)
        print("You Won")
        result.append("You Won")
    if choice=='Water' and a=='Gun':
        print(choice, "V/s", a)
        print("You Won")
        result.append("You Won")
    if choice=='Gun' and a=='Water':
        print(choice, "V/s", a)
        print("You Loose")
        result.append("You Loose")
    i=i+1
    print("The No Of Chances Left Is",5-i)
    #print(result)
    win=result.count("You Won")
    draw=result.count("Draw")
    loose=result.count("You Loose")
    if i==5:
        print("=====================================================================================================================================================================")
        print("The No Of Win is:",win)
        print("The No Of Draw is:",draw)
        print("The No Of Loose is",loose)
        print("=====================================================================================================================================================================")
    if win>=3:
        print("Congrat's You Won")
        break
    if win==2 and loose==2 and draw==1:
        print("It was a Draw")
        break
    if draw==2 and win==1 and loose==1:
        print("It is Draw")
        break
    if draw>=3:
        print("It is a Draw")
    if loose>=3:
        print("Sorry you lost")
        break
