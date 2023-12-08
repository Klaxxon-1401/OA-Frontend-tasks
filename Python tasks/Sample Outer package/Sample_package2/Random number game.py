import random
b=random.randint(1,5)

n=int(input('Enter a number between 1 and 5: '))
if(n<=5):
    while(n!=b):
        n=int(input('Enter a number between 1 and 5: '))
        b=random.randint(1,5)
        if(n==b):
            print('You win ')
        else:
            print('You lose')
        
else:
    print('Invalid Number')
