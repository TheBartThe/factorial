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

##    for i in range(1, (factorial+1)):
##        factorial /= i
##        if factorial == 1:
##            return i
##    return "NONE"

        
    product = 1
    i = 2
    while (product < factorial):
        product *= i
        if (product == factorial):
            return i
        elif (product > factorial):
            return "NONE"
        i += 1
