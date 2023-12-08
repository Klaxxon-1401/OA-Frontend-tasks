eng=int(input('Enter English Mark'))
math=int(input('Enter Maths Mark'))
sci=int(input('Enter Science Mark'))
scs=int(input('Enter Social Science Mark'))


if (eng>=40 and math>=40 and sci>=40 and scs>=40):

    
    if(eng>80 and math>80 and sci>80 and scs>80):
        print('Science Stream')

    elif(eng>=80 and math>=50 and sci>=50):
        print('Commerce Stream')

    elif(eng>=80 and scs>=80):
        print('Humanities Stream')



else:
    print('You are required to pass in order to apply')
