def factorial(factorial):
##    while(True):
##        try:
##            factorial = int(input("Enter your factorial: "))
##            if (factorial < 1):
##                print("Too low, factorial must be greater than zero")
##                continue
##            break
##        except ValueError:
##            print("Invalid Input")
##            continue

        
    product = 1
    i = 2
    while (product < factorial):
        product *= i
        if (product == factorial):
            return i
        elif (product > factorial):
            return "NONE"
        i += 1
