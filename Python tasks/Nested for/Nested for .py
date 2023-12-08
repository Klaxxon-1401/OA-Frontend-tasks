
temp=0
for i in range(1,5):
    for j in range(1,5):
        if(i>=j):
            print(j, end=' ')
    temp=temp+j  
    print(temp)

