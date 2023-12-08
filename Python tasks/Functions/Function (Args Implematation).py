def Add(*a):
    list1=list(a)
    l=0
    for i in list1:
        l=i+l
    print('The Sum of the given Numbers  is:',l )

Add(3,4,5,6)
Add(2,3,4,5,6,7)
print('\n')

def bla(a='bruh'):
    print(a)
bla('yooooooooooo')
bla()
print('\n')
    
def somefunct(a,b,v):
    print(a,b,v,)

somefunct(b=17,a=19,v=27) 
print('\n')


def vivalarevolucion(**n):
    print(n)

vivalarevolucion(a=17,b=19,c=14)
