class mathematical:
    def __init__(self, a):
        self.a = a

    def cal_max(self):
        Max = self.a[0]
        for i in self.a:
            if i>Max:
                Max = i
        return Max

    def cal_min(self):
        Min = self.a[0]
        for i in self.a:
            if i<Min:
                Min = i
        return Min

    def cal_avg(self):
        Sum = 0
        for i in self.a:
            Sum = Sum+i
        return Sum/len(self.a)

    def cal_var(self):
        
        avg = self.cal_avg()
        Sum = 0
        for i in self.a:
            Sum = Sum+(i-avg)**2

        return Sum/len(self.a)
    

class rect:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def area(self):
        return self.w*self.l
    
    def primeter(self):
        return 2*(self.w+self.l)
    