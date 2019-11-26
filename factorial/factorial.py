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
    for i in range(1, (factorial+1)):
        factorial /= i
        if factorial == 1:
            return i
    return "NONE"

        
