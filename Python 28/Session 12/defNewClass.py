class mathOperations():
    def __init__(self, numbers):
        self.numbers = numbers

    def calAverage(self):
        Sum = 0
        for i in self.numbers:
            Sum = Sum + i
        return Sum / len(self.numbers)
    
    def calVariance(self):
        avg = self.calAverage()
        Sum = 0
        for i in self.numbers:
            Sum = Sum + (i-avg)**2
        return Sum / len(self.numbers)
    
    def calMin(self):
        Min = self.numbers[0]
        for i in self.numbers:
            if Min > i:
                Min = i
        return Min
    
    def calMax(self):
        Max = self.numbers[0]
        for i in self.numbers:
            if Max < i:
                Max = i
        return Max