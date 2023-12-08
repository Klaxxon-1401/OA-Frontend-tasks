class Trucks():
    def __init__(s,name,brand,horsepower,maxrpm,maxloadcapacity,mileage):
        s.name=name
        s.brand=brand
        s.horsepower=horsepower
        s.maxrpm=maxrpm
        s.maxloadcapacity=maxloadcapacity
        s.__mileage=mileage
    def Transport(s):
        print(s.name,'Can be used for transport')
    def Loadbearing(s):
        print(s.name,'Can be used for load bearing ')
    def displayprop(s):
        print('Name ',s.name)
        print('Brand ',s.brand)
        print('Horsepower ',s.horsepower)
        print('Max RPM',s.maxrpm)
        print('Load Capacity',s.maxloadcapacity)
    def mileageget(s):
        print('Mileage',s.__mileage)
        
class Cars(Trucks):
    def __init__(s,name,brand,horsepower,maxrpm,stopto60time,topspeed,gears):
        s.name=name
        s.brand=brand
        s.horsepower=horsepower
        s.maxrpm=maxrpm
        s.stopto60time=stopto60time
        s.topspeed=topspeed
        s.gears=gears
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
    def displayprop(s):
        print('Name ',s.name)
        print('Brand ',s.brand)
        print('Horsepower ',s.horsepower)
        print('0 to 60 time ',s.stopto60time)
        print('Topspeed ',s.topspeed)
        print('Gears ',s.gears)
class Bikes(Cars):
    def Ride(s):
        print(s.name,'can be used to ride')
    def Wheelie(s):
        print(s.name,'can do stoppies and wheelies')
a3=Trucks('F150','Ford',325,7000,898,60)        
a1=Cars('Zonda','Pagani',700,7500,8,389,6)
a2=Bikes('Ninja H2R','Kawasaki',305,14000,2.5,400,6)
print('Truck')
a3.displayprop()
print('\nCar:')
a1.displayprop()
print('\nBike:')
a2.displayprop()
a3.mileageget()

