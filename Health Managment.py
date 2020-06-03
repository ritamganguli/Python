print("Welcome To The Health Managment App")
print("------------------------------------")
print("Press 1 for Harry ")
print("Press 2 for Rituja")
print("Press 3 for Ritam")
print("What you want to lock:")
print("-----------------------")
def func():
    print("Press 1 for Diet")
    print("Press 2 for Exersise")

press=int(input())
if press==1:
    print("You Choosed Harry")
    func()
    key1=int(input())
    if key==1:
        print("You Choosed Diet")
        print("-----------------")
        print("Please Enter The Diet Taken")
        diet1=input()
        f=open("HarryDiet.txt","a")
        f.write("\n")
        f.write(diet1)
        f.write(" ")
        f.write(":")
        f
