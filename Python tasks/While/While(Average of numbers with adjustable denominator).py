n=int(input('Enter N Value'))
l=n
a=0
while(n>0):
    m=int(input('Enter Subject Mark'))
    a=m+a
    b=a//l
    n=n-1
print('The average is:',b)

