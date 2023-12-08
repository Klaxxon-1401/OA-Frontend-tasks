num = int(input("Enter a Number"))
num2=0
while num!=0:
    variable1=num%10
    num2=num2*10+variable1
    num=num//10

print('The reversed number is:',num2)



