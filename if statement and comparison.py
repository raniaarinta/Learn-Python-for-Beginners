def max_num(num1,num2,num3):
    if(num1>= num2) and (num1>= num3):
        return num1
    elif (num2>=num1) and (num2 >= num3):
        return num3 
    elif(num3>=num1) and (num3 >= num2):
        return num3
    
number1= input("input first number: ")
number2= input("input second number: ")
number3= input("input thrird number: ")

result= max_num(number1,number2,number3)
print ("maximum number : " +result)