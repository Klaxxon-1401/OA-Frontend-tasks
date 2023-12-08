Time=input('Enter Railway Time : ')
Day=input('Enter Day (Short form)')
Duration=input('Enter Duration')

time1=Time[0]+Time[1]
time2=Time[3]+Time[4]
time3=int(time1+time2)

dur=int(Duration[0]+Duration[1])
dur3=int(Duration[3])+int(Duration[4])
dur4=int(dur)


if(dur>1):
    dur2=int(dur)*60+dur3
else:
    dur2=int(Duration)    

if(Day=='Mon' or Day=='Tue' or Day=='Wed' or Day=='Thu' or Day=='Fri'):
    if(time3>=700 and time3<=1800):
            n=dur2*1.25
            print(n)
    elif(time3>1800 or time3>0000 and time3<700):
            n=dur2*1.15
            print(n)
            
elif(Day=='Sun' or Day=='Sat'):
        m=dur2*1.15
        print(m)
