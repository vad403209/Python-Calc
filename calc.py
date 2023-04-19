i=0

while i==0:
    op = input("Choose an operator (+,-,*,/,%, 1 to exit): ")
   
    if op=='+':
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the second Number: "))
        result = str(num1 + num2)
        print("The result is " + result)
    elif op=='-':
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the second Number: "))
        result = str(num1 - num2)
        print("The result is " + result)
    elif op=='*':
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the second Number: "))
        result = str(num1 * num2) 
        print("The result is " + result)   
    elif op=='/':
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the second Number: "))
        result = str(num1 / num2)
        print("The result is " + result)
    elif op=='%':
        num1 = int(input("Enter the first Number: "))
        num2 = int(input("Enter the second Number: "))
        result = str(num1 % num2)
        print("The result is " + result)
    elif op=='1':
        i = 1
        print("Calculator exited!")
    else:
        print("Invalid input")
