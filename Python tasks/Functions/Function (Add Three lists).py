list1=[1,2]
list2=[3,4]
list3=[5,6]

def funct(n,m,k):
    return n+m+k


x=map(funct,list1,list2,list3)
print(list(x))
    
