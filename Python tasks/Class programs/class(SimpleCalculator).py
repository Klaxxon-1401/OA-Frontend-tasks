class Calculator():
    firstNumber=10
    secondNumber=5
    def getFirstNum(self):
        print('First Num = ',self.firstNumber)
    def getSecondNum(self):
        print('Second Num = ',self.secondNumber)
    def getAdditionResult(self):
        print('Addition Result = ',self.firstNumber+self.secondNumber)
    def getSubtractionResult(self):
        print('Subtraction Result = ',self.firstNumber-self.secondNumber)
    def getMultiplicationResult(self):
        print('Multiplication Result = ',self.firstNumber*self.secondNumber)
    def getDivisionResult(self):
        print('Division Result = ',self.firstNumber/self.secondNumber)


c1=Calculator()
c1.getFirstNum()
c1.getSecondNum()
c1.getAdditionResult()
c1.getSubtractionResult()
c1.getMultiplicationResult()
c1.getDivisionResult()
