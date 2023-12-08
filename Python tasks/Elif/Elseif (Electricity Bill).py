

NOU=int(input('Enter The Number Of Units Used'))
##NOU= Number Of Units


if(NOU<100):
        price=((NOU)*0)
        print('Your Electricity Bill =',price)

elif(NOU>100 and NOU<=200):     
        price=((NOU-100)*5)
        print('Your Electricity Bill =',price)

elif(NOU>200):
        price=((NOU-150)*10)
        print('Your Electricity Bill =',price)




