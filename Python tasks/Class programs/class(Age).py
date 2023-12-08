class Person():
    Name='Dave'
    Country='Canada'
    Yearofbirth=1987
    def Agecalc(s,cy):
        print ('Age = ',cy-s.Yearofbirth)

YOB=int(input('Enter your Year of Birth: '))

currentyear=2023
a1=Person()
a1.Yearofbirth=YOB
a1.Agecalc(currentyear)
