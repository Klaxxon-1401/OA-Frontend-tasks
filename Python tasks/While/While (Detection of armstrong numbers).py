
    
num=int(input("Enter a Number:"))
num2=0
num2=num
Sum=0
while (num>0):
    
    remainder=num%10
    num=num//10
    variable1=remainder**3
    print(variable1)
    Sum = Sum+variable1  
print("Sum of The Cubes of  The Digits: ", Sum)
    

if(Sum==num2):
    print('The given number is an armstrong number')

else:
    print('The given number is not an armstrong number')
































