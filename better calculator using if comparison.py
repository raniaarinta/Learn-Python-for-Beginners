def addition_num(num1, num2):
    return num1+num2
def subtraction_num(num1, num2):
    return num1-num2
def multiply_num(num1, num2):
    return num1*num2
def division_num(num1,num2):
    return num1/num2

def check_operator(operator_type,num1,num2):
    if(operator_type == "+"):
        print(addition_num(num1,num2))
    elif(operator_type=="-"):
        print(subtraction_num(num1,num2))
    elif(operator_type=="*"):
        print(multiply_num(num1,num2))
    elif(operator_type=="/"):
        print(division_num(num1,num2))
    else:
        print("invalid operator")

operator= input("choose your calculator operation: ")
value1=input("enter first value ")
value2=input("enter second value ")
check_operator(operator,float(value1),float(value2))
        
    
    