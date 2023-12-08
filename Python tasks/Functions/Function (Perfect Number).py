n=int(input('Enter integer'))
def num_perfect(num):  
    sum_n = 0  
    for i in range(1, num):  
        if num % i == 0:  
            sum_n=sum_n+i  
    return sum_n == num


if num_perfect(n) == True  :
    print('The given number is a perfect number')
else:
    print('The given number is not a perfect number')



        
    
