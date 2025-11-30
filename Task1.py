#This is a python program which uses function to make a calculator.

#Creating function
def calculator(num1,num2,operator):
    if operator == "+":
        print("The sum of ",num1 ," and ",num2," is:",num1 + num2 )
    elif operator == "-":
        print("The difference of ",num1 ," and ",num2," is: ", num1 - num2)
    elif operator == "*":
        print("The product of ",num1 ," and ",num2," is: ", num1 * num2)
    elif operator == "/":
        if(num2 == 0):
            print("Division by zero is not possible.")
        else:    
            print("The division of ",num1 ," and ",num2," is: ", num1 / num2)

    else:
        print("Invalid operator.")

#Main body of program
print("-------------------------------------------------")
print("                    Calculator                   ")
print("-------------------------------------------------")

#Prompting user to enter the values and operator.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter the operator: ")

calculator(num1,num2,operator)