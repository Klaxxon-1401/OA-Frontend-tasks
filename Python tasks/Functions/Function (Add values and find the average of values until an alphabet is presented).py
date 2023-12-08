def funct1(a):
    l=0
    count=0
    b=input('Enter Numbers:' )
    if(b.isalpha()==False):
        while(b.isalnum()==True):
            count+=1
            n=input('Enter Numbers:' )
            if(n.isalpha()==True):
                break;
            l=int(b)+int(n)+l
        print('Sum =',l)
        print('Average =',l/count)
        
funct1(3)
