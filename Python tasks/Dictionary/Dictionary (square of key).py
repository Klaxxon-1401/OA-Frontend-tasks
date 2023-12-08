v=['1','2','3','4','5','6','7','8']
n=[1,2,3,4,5,6,7,8]
for i in range(len(n)-1):
    
    m=n[i]**n[i]
    l=v[i]
    dict1=dict.fromkeys(l,m)
    print(dict1)
