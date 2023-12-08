class Calculator():
    def add(s,a,b):
        return a+b
    def subtract(s,a,b):
        return a-b
    def multiply(s,a,b):
        return a*b
    def divide(s,a,b):
        return a/b
    


x=int(input('enter a value '))
y=int(input('enter another value '))

a1=Calculator()
print('Sum',a1.add(x,y))
print('Difference',a1.subtract(x,y))
print('Product',a1.multiply(x,y))
print('Quotient',a1.divide(x,y))
