numdict={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
n=int(input('Enter the number'))
list1=[]
l=0
while(n>0):
    l=n%10
    n=n//10
    list1.append(l)
list1.reverse()
for i in list1:
    print(numdict[i] , end=' ')

























##numdict={'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
##b=' '
##n=input('Enter Number')
##for i in n :
##    b=b+' '+numdict[i]
##
##print(b)
##    
