Age=int(input('Enter Age'))
Gender=input('Enter Gender')


if(Age>=18 and Age<=40):
    
        if(Age>=18 and Age<30 and Gender=='Male' or Gender == 'male'):
             print('Your Wage Per Day Is = 700' )

        elif(Age>=18 and Age<30 and Gender=='Female' or Gender== 'female'):
                print('Your Wage Per Day Is = 750')

        elif(Age>=30 and Age<=40 and Gender=='Male'or Gender=='male'):
                print('Your Wage Per Day Is = 800')

        elif(Age>=30 and Age<=40 and Gender=='Female' or Gender=='female'):
                print('Your Wage Per Day Is = 850')

else:
    print('Please Enter Appropriate Age')
