import numpy as np

def data(x):
        a = x[0,:]
        b = x[1,:]
        print(a)
        print(b)
        if len(a)>=11:
                l = 10
        else:
                l = len(a)-1
        c = np.zeros((l,1))
        print(c)
        
        for y in range(1,l):
                pf = np.polyfit(a,b,y)
                value = np.polyval(pf,a)
                c[y-1,0] = np.linalg.norm(b-value)
                z = c.argmin()
                data = np.polyfit(a,b,z+1)
                print(data)
                print('Best Approximate Data, Coefficients of the Polynomial: \n',data)
      
data(np.array([(5,7,36,9,4,15,8,45,87,95,63,12),(8,98,6,3,2,52,41,63,89,75,91,62)])) # Given array
