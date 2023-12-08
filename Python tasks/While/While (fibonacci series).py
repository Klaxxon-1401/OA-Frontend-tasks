a= int(input("Enter the No. of terms:"))

x=0
y=1
l=0

print('\n')

print("Fibonacci sequence:")
while l< a:
    print(x)
    z=x + y
    x=y
    y=z
    l+=1
