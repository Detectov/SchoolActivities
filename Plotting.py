import math 
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, numpoints):
        self.numpoints = numpoints
        self.xvalues = []
        self.yvalues = []
        
    def pointcalc(self):
        for i in range(self.numpoints):
            x = i * 10 / (self.numpoints - 1) - 5
            y = math.exp(-abs(x)) * math.cos(2 * math.pi * x)
            self.xvalues.append(x)
            self.yvalues.append(y)
            
    def plott(self):
        plt.plot(self.xvalues, self.yvalues)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    
numpoints = int(input("Enter the numbers that you want to plot: "))
plotting = Plot(numpoints)
plotting.pointcalc()
plotting.plott()