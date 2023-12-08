

Salary=int(input('Enter Your Salary'))
Years=int(input('Enter Your Years Of Service'))

if (Years>10):
    Bonus=(10/100*Salary)
    print('Your Total Salary Amount Is =',Salary+Bonus)

            
elif(Years>=6 and Years <=10):
    Bonus=(8/100*Salary)
    print('Your Total Salary Amount Is =',Salary+Bonus)

elif(Years<6):
     Bonus=(5/100*Salary)
     print('Your Total Salary Amount Is =',Salary+Bonus)
