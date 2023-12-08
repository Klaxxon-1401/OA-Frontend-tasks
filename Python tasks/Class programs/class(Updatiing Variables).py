class Car():
    Name='Jeep Wrangler'
    TopSpeed=50
    def getname(self):
        print(self.Name)
    def gettopspeed(self):
        print(self.TopSpeed)
    def setname(self,a):
        self.Name=a
    def settopspeed(self,a):
        self.TopSpeed=a
    def gettopspeedkmh(self):
        kmhspeed=self.TopSpeed*3.666
        print(kmhspeed)
        
        



print('Before Changes')
c1=Car()
c1.getname()
c1.gettopspeed()
c1.gettopspeedkmh()

print('\nAfter Changes')
c1.setname('Jeep Cherokee')
c1.settopspeed(40)
c1.getname()
c1.gettopspeed()
c1.gettopspeedkmh()


