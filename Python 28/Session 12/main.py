from defNewClass import mathOperations

class Fatemeh(mathOperations):
    def calSTD(self):
        var = self.calVariance()
        return var**0.5

numbers = [5, 7, 18, 17, 2, 9.75]
math = Fatemeh(numbers)

print(math.calAverage())
print(math.calVariance())
print(math.calMin())
print(math.calMax())
print(math.calSTD())