def calculate(num1,num2,operator):
    if (operator == "+"): 
        return num1+num2
    elif (operator == "-"):
        return num1-num2
    elif (operator == "/"):
        return num1/num2
    elif (operator == "*"):
        return num1*num2
    elif (operator == "^"):
        return num1**num2
    

    else:
        return("Invalid operator")

n1 = float(input('Enter a number:  '))
op = input("Enter the operator\n (a)+ \n (b)- \n (c)* \n (d)/ \n (e)^ \n")
n2 = float(input("Enter the second number:  "))

c=calculate(n1,n2,op)
print(f"your calculation :\n {n1} {op} {n2} = {c}")