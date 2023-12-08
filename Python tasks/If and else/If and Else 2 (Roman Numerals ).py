dict1={'I':1,'II':2,'III':3,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

n=input('Enter the roman numerals')
l=0

for j in range(0,len(n),2):
    c=n[j]

    
for i in n:
    b=dict1.get(n)
    l=l+b
    
if(c=='I' and i=='V' or c=='I' and i=='X'):
    l=l-2
elif(c=='X' and i=='L' or c=='X' and i=='C'):
    l=l-20
elif(c=='C' and i=='D' or c=='C' and i=='M'):
    l=l-200

print(l)



