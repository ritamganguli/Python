print("For Harry chose 1\nFor Rituja choose 2\nFor Ritam choose 3")
number=int(input())
if number==1:
    print("You Choosed Harry\n")
    print("For diet press 1\nFor Exersise Press 2")
    number1=int(input())
    if number1==1:
        print("You Choosed Diet\nPlease enter the diet taken")
        food1=input()
        print("At What day")
        time=input()
        f=open("HarryDiet.txt", "a")
        f.write("\n")
        f.write(food1)
        f.write(" ")
        f.write(":")
        f.write(time)
    if number1==2:
        print("You choosed exersise please enter the exersise done")
        exe1=input()
        print("At what day")
        time1=input()
        m=open("HarryExersise.txt","a")
        m.write("\n")
        m.write(exe1)
        m.write(" ")
        m.write(":")
        m.write(time1)
if number==2:
    print("You Choosed Rituja\n")
    print("For diet press 1\nFor Exersise Press 2")
    number2 = int(input())
    if number2==1:
        print("You Choosed Diet\nPlease enter the diet taken")
        food2=input()
        print("At what date")
        time2=input()
        f = open("RitujaDiet.txt", "a")
        f.write("\n")
        f.write(food2)
        f.write(" ")
        f.write(":")
        f.write(time2)
    if number2 == 2:
        print("You choosed exersise please enter the exersise done")
        exe2 = input()
        print("At what date")
        time4=input()
        m = open("RitujaExersise.txt", "a")
        m.write("\n")
        m.write(exe2)
        m.write(" ")
        m.write(":")
        m.write(time4)
if number==3:
    print("You Choosed Ritam\n")
    print("For diet press 1\nFor Exersise Press 2")
    number3 = int(input())
    if number3 == 1:
        print("You Choosed Diet\nPlease enter the diet taken")
        food3 = input()
        print("At what date")
        time5=input()
        f = open("RitamDiet.txt", "a")
        f.write("\n")
        f.write(food3)
        f.write(" ")
        f.write(":")
        f.write(time5)
    if number3 == 2:
        print("You choosed exersise please enter the exersise done")
        exe3 = input()
        print("at what day he did")
        time3=input()
        m = open("RitamExersise.txt", "a")
        m.write("\n")
        m.write(exe3)
        m.write(" ")
        m.write(":")
        m.write(time3)

