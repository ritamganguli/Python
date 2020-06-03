print("Lets Play The No Guessing Game")
print("Guess The No Between 1 to 100")
print("Please Enter Your No")
choise=5
while(True):
    num = int(input())

    if num>18:
        print("Please Guess A Lesser No")
        choise=choise-1
        print("The no of Choise Left Is",choise)
    if num<18:
        print("Please Guess A Larger No\n")
        choise=choise-1
        print("The No Of Choise Left Is",choise)
    if num==18:
        print("You Guess The Right No")
        print("The No of Choise Left Was ",choise )
        break
    if choise==0:
        print("You Have Exhausted Maximum Limit")
        break


