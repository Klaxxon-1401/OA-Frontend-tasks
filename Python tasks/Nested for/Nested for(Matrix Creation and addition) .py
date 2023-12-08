a=[]
b=[]


r=int(input('Enter row value'))
c=int(input('Enter column value'))


for i in range(r):
    a.append([ ])
    b.append([])
    for j in range(c):
        m=int(input('Enter Value'))
        a[i].append(m)
        b[i].append(m+1)
        
 

for i in range(c):
    for j in range(r):
        l=a[i][j]+b[i][j]
        print(l,'',end='')
    print('')
