def factorial(x):
    if (x != 1):
        return (x * factorial(x-1))  
    else:
        return 1

num = 3
print("The factorial of", num, "is", factorial(num))
