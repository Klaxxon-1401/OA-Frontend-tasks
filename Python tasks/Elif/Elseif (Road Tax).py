CostPrice=int(input('Enter The Cost Price'))

if(CostPrice>100000):
    Tax=(15/100*CostPrice)
    print('The Road Tax For The Vehicle Is ,Rs',Tax)

    
elif(CostPrice>50000 and CostPrice<=1000000):
    Tax=(10/100*CostPrice)
    print('The Road Tax For The Vehicle Is ,Rs',Tax)

elif(CostPrice<=50000):
    Tax=(5/100*CostPrice)
    print('The Road Tax For The Vehicle Is ,Rs',Tax)
    
