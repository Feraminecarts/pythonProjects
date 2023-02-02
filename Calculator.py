from math import *


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def fact(x):
    duplicate = x
    for i in range(1, x):
        x *= (duplicate-i)
    return x


def calc(x, y=None):
    if opr == "+":
        return add(x, y)
    elif opr == "-":
        return subtract(x, y)
    elif opr == "*":
        return multiply(x, y)
    elif opr == "/":
        return divide(x, y)
    elif opr == "sin()":
        return sin(x)
    elif opr == "cos()":
        return cos(x)
    elif opr == "tan()":
        return tan(x)
    elif opr == "ln()":
        return log(x)
    elif opr == "log()":
        return log(x, 10)
    elif opr == "^":
        return pow(x, y)
    elif opr == "sqrt()":
        return sqrt(x)
    elif opr == "!":
        return fact(x)
    else:
        print("Please enter a valid input")


print("")
print("---------CALCULATOR---------")
print("")
done = "no"
result = 0
contcalc = "no"

while done == "no":
    if contcalc == "no":
        fn = int(input("Input First Number >>"))
    elif contcalc == "yes":
        fn = result
    else:
        fn = int(input("Input First Number >>"))
    opr = input(
        "Enter the Operation you want to perform [+, -, *, /, sin(), cos(), tan(), ln(), log(), ^, sqrt(), !] >>").lower()
    if opr == "sin()" or opr == "cos()" or opr == "tan()" or opr == "ln()" or opr == "log()" or opr == "sqrt()" or opr == "!":
        result = calc(fn)
        print(f"Result = {result}")
        done = input("Would you like to stop? ('yes' or 'no') >>").lower()
        if done == "yes":
            break
        contcalc = input("Would you like to continue operations on result? ('yes' or 'no') >>").lower()
        continue
    sn = int(input("Input second Number >>"))
    result = calc(fn, sn)
    print(f"Result = {result}")
    done = input("Would you like to stop? ('yes' or 'no') >>")
    if done == "yes":
        break
    contcalc = input("Would you like to continue operations on result? ('yes' or 'no') >>").lower()

print("Thank you for using the calculator! Hope you enjoyed!")
