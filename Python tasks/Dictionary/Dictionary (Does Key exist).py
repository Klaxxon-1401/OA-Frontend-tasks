dict1={1:1,2:2,3:3}
a=dict1.keys()
key=int(input('Enter Key value'))

if(key in a):
    print('Key exists in dictionary')
else:
    print('Key does not exist in dictionary')
