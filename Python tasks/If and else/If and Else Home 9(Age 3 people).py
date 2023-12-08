A1=int(input('Enter Age 1:'))
A2=int(input('Enter Age 2:'))
A3=int(input('Enter Age 3:'))


if A1>A2 and A1>A3:
    print('Age 1 is the highest')

elif A2>A1 and A2>A3:
    print('Age 2 is the highest')

elif A3>A1 and A3>A2:
    print('Age 3 is the highest')

if A1<A2 and A1<A3:
    print('Age 1 Is The Lowest')

elif A2<A1 and A2<A3:
    print('Age 2 Is The Lowest')

else:
    print('Age 3 Is The Lowest')
