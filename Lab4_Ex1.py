class Cylin():
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def calculate(self):
        self.Measure = 3.141 *(self.Radius*self.Radius)*self.Height
        return self.Measure 
    
Cylin1 = Cylin(5,10)
Cylin2 = Cylin(7,13)
print("First Cylin Measure is = " +str (Cylin1.calculate()))
print("Second Cylin Measure is = " +str(Cylin2.calculate()))
