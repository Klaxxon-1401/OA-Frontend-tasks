def Well(a):
    print('Well is empty')
    a()
    print('Well is Full')
    def Well2():
        print('Turn off Pump')
    return  Well2
@Well    
def Pump():
    print('Pump is running')

x=Well(Pump)
x()



Pump()


