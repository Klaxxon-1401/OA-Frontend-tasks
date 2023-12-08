dict1={1:11,2:22,3:33,4:44}
dict2={1:11,5:55,6:66}
dict3=dict1.copy()
a=len(dict1)
b=list(dict1.values())
c=list(dict2.values())

for i in b:
    if(i in c):        
        n=dict3.update({a+1:i})
        print('Dictionary 1:',dict1)
        print('Dictionary 2:',dict2)
        print('Final Dictionary',dict3)
    

