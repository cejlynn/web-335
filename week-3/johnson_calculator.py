# ==============================================
# ; Title: johnson_calculator.py
# ; Author: Caitlynne Johnson
# ; Date: 31 March 2023
# ; Description: Experimenting with Python variables and functions.

# =============================================


    #functions with two parameters that will add, subtract, divide, and multiply

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y 
    
def multiply(x, y):
    return x * y
    
    #add variables 
num1 = 4
num2 = 4


    #tests the add function
add_result = f"{num1} + {num2} is {add(num1, num2)}"

    #subtract variables
num3 = 10
num4 = 6

    #tests the subtract function
subtract_result = f"{num3} - {num4} is {subtract(num3, num4)}"

    #divide variables
num5 = 8
num6 = 2

    #tests the divide function
divide_result = f"{num5} / {num6} is {divide(num5, num6)}"

    #multiply variables
num7 = 10
num8 = 2

    #tests the multiply function
multiply_result = f"{num7} * {num8} is {multiply(num7, num8)}"

    #calls each function
print(add_result)
print(subtract_result)
print(divide_result)
print(multiply_result)