Year=int(input('Enter Year'))

if(Year%100==0 ):
    if(Year%400==0):
        print('The Given Year Is A Leap Year')
    else:
        print('The Given Year Is Not A Leap Year')
else:
    if(Year%4==0):
         print('The Given Year Is A Leap Year')
    else:
         print('The Given Year Is Not A Leap Year')

    
