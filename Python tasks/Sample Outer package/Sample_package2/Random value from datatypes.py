import random
list1=[1,2,3,4,5,6,]
set1={1,2,3,4,5,5,6,7,8}
dict1={1:1,2:2,3:3}
x=list(dict1.keys())
setlist=[]

for i in set1:
    setlist.append(i)

a=random.choice(list1)
b=dict1[random.choice(x)]
c=random.choice(setlist)


print('Random list value= ',a)
print('Random dictionary value = ',b)
print('Random set value= ',c)
          

