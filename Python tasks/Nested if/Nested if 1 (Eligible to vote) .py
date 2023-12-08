Age=int(input('Enter Age'))

if(Age>0 and Age<100):
    if(Age>18):
        print('Eligible')
    else:
        print('Not Eligible')
else:
    print('Invalid Input')
