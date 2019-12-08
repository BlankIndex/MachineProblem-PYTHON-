from matplotlib import pyplot as prot
import math

# x = x of n
# y = y of n
def x(n):
    return math.sin((3*math.pi*n)/100)
def y(n): # Piecewise Function
    if n==0:
        return -1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
    elif n>0 and n<=198:
        return 0.5*x(n+1) - 0.5*x(n-1)
    elif n<=198:
        return 1.5*x(n) - 2*x(n-1) + 0.5*x(n-2)
    
l_values = list(range(200))
x_values = [x(n) for n in l_values]
y_values = [y(n) for n in l_values]

prot.grid()
prot.plot(l_values,x_values,label = 'Value of x(n)') # x(n) Graph
prot.plot(l_values,y_values,label = 'Value of y(n)') # y(n) Graph
prot.legend() # adds legend
prot.show() # showing of Graph
