class Python27:
    def __init__(self, numbers) :
        self.numbers = numbers
    
    def calAverage(self):
        Sum = 0
        for i in self.numbers:
            Sum = Sum + i
            
        return Sum / len(self.numbers)
    
    def calVariance(self):
        Sum = 0
        avg = self.calAverage()
        for i in self.numbers:
            Sum = Sum + (i-avg)**2
            
        return Sum / len(self.numbers)
    
    def calMax(self):
        Max = self.numbers[0]
        for i in self.numbers:
            if i>Max:
                Max = i
                
        return Max
    
    def calMin(self):
        Min = self.numbers[0]
        for i in self.numbers:
            if i<Min:
                Min = i
                
        return Min
    
    def calSTD(self):
        var = self.calVariance()
        
        return var**0.5
    
    
class Python27_2:
    def __init__(self) :
        pass
    
    def calAverage(self, numbers):
        Sum = 0
        for i in numbers:
            Sum = Sum + i
            
        return Sum / len(numbers)
    
    def calVariance(self, numbers):
        Sum = 0
        avg = self.calAverage(numbers)
        for i in numbers:
            Sum = Sum + (i-avg)**2
            
        return Sum / len(numbers)
    
    def calMax(self, numbers):
        Max = numbers[0]
        for i in numbers:
            if i>Max:
                Max = i
                
        return Max
    
    def calMin(self, numbers):
        Min = numbers[0]
        for i in numbers:
            if i<Min:
                Min = i
                
        return Min
    
    def calSTD(self, numbers):
        var = self.calVariance(numbers)
        
        return var**0.5
    
    
    