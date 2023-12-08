a=input('Enter Word')
z=int(len(a))
y=int(len(a)-1)
x=int(len(a)-2)
q=int(len(a)-3)


s=(a[q:z])

if(s=='ing'):
    pass
else:
    print(a+'ing')
