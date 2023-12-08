a=input('')
b=len(a)-1


if(len(a)>2):
    z=a.replace(a[0],'')
    print(z.replace(a[b],''))
else:
    print(a)
    


