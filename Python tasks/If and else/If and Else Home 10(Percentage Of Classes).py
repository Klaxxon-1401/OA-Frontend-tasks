Classhd=int(input('Enter The Number of Classes Held '))
Classat=int(input('Enter The Number Of Classes Attended'))

POCA=(Classat/Classhd)*100
POCA=int(POCA)

if (POCA>75):
    print('As You Have Attended ' ,POCA,'Percentage Of Classes Held You Are Allowed To Write The Examination')

else:
    print('As You Have Attended ' ,POCA,'Percentage Of Classes Held You Are Not Allowed To Write The Examination')


