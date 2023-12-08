n=int(input("Enter an integer:"))
i=1
list1=[]
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            list1.append(i)
    i=i+1
    
print('The Largest prime number is ',max(list1))

