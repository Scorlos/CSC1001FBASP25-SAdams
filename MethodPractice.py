# Practicing creating functions
# def (keyword)
# name of your function
# arguement
# return value (optional)

def newLine ():
    print();

def readInput ():
    myInput = input("Enter something: ");
    return myInput;

# readInteger
def readInteger ():
    return int(input("Enter an integer: "));

print("It is Wednesday my dudes");
print(newLine());
lineCatcher = readInput();
print(lineCatcher);
myInteger = readInteger();
print(lineCatcher);

print(type(lineCatcher));
print(type(myInteger));

exit();