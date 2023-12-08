num=int(input('Enter Number:'))
root_num=int(input('Enter Root Number:'))
count=0
while(num!=0):
    num=num//root_num
    if(num!=0):
        count+=1
        pass
print(count)
      
