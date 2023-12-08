##Sum Of N Number of Even Numbers 



n=int(input('Enter A Number:'))
tmp=0
for i in range(2,2*n+1,2):

    tmp=tmp+i
    
print('Sum=',tmp)


##print('Sum =',n*(n+1))
