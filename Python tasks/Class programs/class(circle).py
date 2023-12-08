class Circle():
    def  Area(s,r):
        return 3.14*r**2
    def Perimeter(s,r):
        return 2*3.14*r
    
    


r=int(input('Enter radius value '))

a1=Circle()
print('Area',a1.Area(r))
print('Perimeter',a1.Perimeter(r))
