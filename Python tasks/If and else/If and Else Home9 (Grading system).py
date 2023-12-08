M=int(input('Enter Your Marks'))

if(M<25):
    print('Your Grade Is F')
    
elif(M>=25 and M<=45):
    print('Your Grade Is E')

elif(M>45 and M<=50):
    print('Your Grade Is D')
    
elif(M>50 and M<=60):
    print('Your Grade Is C')

elif(M>60 and M<=80):
    print('Your Grade Is B')

elif(M>80 and M<100):
    print('Your Grade Is A')

elif(M>100):
    print('Invalid Number')
