print("This Is A Calculator")
print("The operation you can use:")
print("For Adittion Press +")
print("For Substraction Press -")
print("For Multiplicatipon Press *")
print("For Divison Press /")
print("\n\nPlease Enter A Number")
num1=int(input())
print("Please Enter Secound Number")
num2=int(input())
print("Enter The Operation To Be Done")
oper=input()
if oper=='*' and num1==45 and num2==3:
    print("The Product is ","555")
elif oper=='+' and num1==56 and num2==9:
    print("The Sum is 77")
elif oper=='/' and num1==56 and num2==6:
    print("The answer is 4")

elif oper=='+':
    print("The Sum is",num1+num2)
elif oper=='-':
    print("The Differance is ",num1-num2)
elif oper=='*':
    print("The Product Is",num1*num2)
elif oper=='/':
    print("The Division Is ",num1/num2)
