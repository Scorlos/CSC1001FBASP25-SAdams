# Addition, Subtraction, Multiplication, and Division Calculator

def addCalc (num1, num2):
    return (num1 + num2);

def subCalc (num1, num2):
    return (num1 - num2);

def multCalc (num1, num2):
    return (num1 * num2);

def divCalc (num1, num2):
    return (num1 / num2);

def calculator ():
    print("What function do you need? \nAddition (1)\nSubtraction (2)\nMultiplication (3)\nDivision (4)")
    selection = int(input("Enter your selection: "));
    if (selection == 1):
        num1 = int(input("Enter an integer: "));
        num2 = int(input("Enter another integer: "));
        print("The sum is " & str(addCalc(num1, num2)));
    if (selection == 2):
        num1 = int(input("Enter an integer: "));
        num2 = int(input("Enter another integer: "));
        print("The difference is " & str(subCalc(num1, num2)));
    if (selection == 3):
        num1 = int(input("Enter an integer: "));
        num2 = int(input("Enter another integer: "));
        print("The product is " & str(multCalc(num1, num2)));
    else:
        num1 = int(input("Enter an integer: "));
        num2 = int(input("Enter another integer: "));
        print("The quotient is " & str(divCalc(num1, num2)));
print("Welcome to the Calculator!");
calculator();
exit();