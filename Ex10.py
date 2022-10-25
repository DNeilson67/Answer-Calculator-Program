choose = input("Equation? (Y/N)")
want =  True

while want == True:
    if choose == "Y":
        eq = input("Input an equation:")
        eq = eval(eq)
        print(f"Here's the results:{eq}")
        wants = input("Continue? (Y/N)")

        if wants == "Y":
            want = True
        elif wants == "y":
            want = True
        elif wants == "N":
            want = False
        elif wants == "n":
            want = False

    elif choose == "N":
        def addition (x,y):
            return x+y

        def subtraction (x,y):
            return x-y

        def multiplication (x,y):
            return x*y
    
        def division (x,y):
            return x/y

        x = int(input("Input the first number:"))
        y = int(input("Input the second number:"))
        print("Operation lists:")
        print('"+" as addition')
        print('"-" as subtraction')
        print('"x" as multiplication')
        print('"/" as division')
        z = str(input("Choose the operation:"))

        if z == "+":
            print(f"Here's the results:{addition(x,y)}")
            wants = input("Continue? (Y/N)")
        elif z == "-":
            print(f"Here's the results:{subtraction(x,y)}")
            wants = input("Continue? (Y/N)")
        elif z == "*":
            print(f"Here's the results:{multiplication(x,y)}")
            wants = input("Continue? (Y/N)")
        elif z == "/":
            print(f"Here's the results:{division(x,y)}")
            wants = input("Continue? (Y/N)")
        else:
            print("me still stupid ya cant")

        if wants == "Y":
            want = True
        elif wants == "y":
            want = True
        elif wants == "N":
            want = False
        elif wants == "n":
            want = False
    
        