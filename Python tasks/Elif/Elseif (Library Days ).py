Days=int(input('Enter The Number Of Days '))

if (Days<=5):
    print('The Fine Levied On You =', Days*2)

elif(Days>=6 and Days<=10):
    print('The Fine Levied On You =', Days*3-5)

elif(Days>=11 and Days<=15):
    print('The Fine Levied On You =', Days*4-15)

elif(Days>15):
    print('The Fine Levied On You =', Days*5-30)
