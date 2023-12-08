class Cars:
    name='Zonda'
    brand='Pagani'
    horsepower=780
    maxrpm=7500
    stopto60time=2.7
    topspeed=375
    gears=6
    def track(s):
        print('The',s.name,'Is fast enough for track')
    def dailydrive(s):
        print('The',s.name,'is reliable enough for daily use')
    def havefun(s):
        print('The',s.name,'Has good handling')
    def propedit(s,n,b,h,st,ts,g):        
        s.name=n
        s.brand=b
        s.horsepower=h
        s.stopto60time=st
        s.topspeed=ts
        s.gears=g
    def displayprop(s,d):
        print('Name ',s.name)
        print('Brand ',s.brand)
        print('Horsepower ',s.horsepower)
        print('0 to go time ',s.stopto60time)
        print('Topspeed ',s.topspeed)
        print('Gears ',s.gears)
a1=Cars()
print('Before changes')
a1.displayprop('s')
a1.propedit('Gallardo','Lamborgini',890,2.05,380,7)
print('\nAfter Changes' )
a1.displayprop('s')

