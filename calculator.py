def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def division(x,y):
    return x/y

print("-------------------------------------")


options = input({
    "+" : "add",
    "-" : "substract",
    "/" : "division"
})

if options != "+" or "-" or "/":
    print("Invalid Input")
    

print("-------------------------------------")

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))

print("-------------------------------------")


if options == "+":
    print("x+y= ", add(num1,num2))

elif options == "-":
    print("x-y= ", substract(num1,num2))

elif options == "/":
    print("x/y= ", division(num1,num2))



print("-------------------------------------")
