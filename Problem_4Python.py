import numpy as penpen
import matplotlib.pyplot as grapher

# Input Values
hi = float(input("The Initial Height of the Projectile above the Ground in meters: "));
vo = float(input("The Magnitude of the Velocity in m/s: "));
theta = float(input("The Angle in Degrees with Respect to the +x-axis: "));
ax = float(input("The x-Component of the Acceleration, Considering the sign, in m/s^2: "));
ay = float(input("The y-Component of the Acceleration, Considering the sign, in m/s^2: "));

if ay == 0:
    print("Error: No Free Fall") # ay can't be 0

theta=theta*(penpen.pi/180);

distance = penpen.sqrt((vo*penpen.sin(theta))**2 - 4*(1/2*ay)*hi);
tcomp = (-vo*penpen.sin(theta) + distance )/ ay;

if tcomp <= 0 :
   tmax = (-vo*penpen.sin(theta) - distance )/ ay;
   t = penpen.linspace(0,tmax,);
   x = vo*penpen.cos(theta)*(t) + 1/2*ax*(t)**2;
   y = vo*penpen.sin(theta)*(t) + 1/2*ay*(t)**2;
else:
        x = vo*penpen.cos(theta)*penpen.linspace(0,tcomp) + (1/2)*ax*penpen.linspace(0,tcomp)
        y = vo*penpen.sin(theta)*penpen.linspace(0,tcomp) + (1/2)*ay*penpen.linspace(0,tcomp);
                          
        
grapher.xlabel('Path of the projectile in the x axis over time')
grapher.ylabel('Path of the projectile in the y axis over time')
grapher.title('Path of the Projectile')
grapher.plot(x,y) # Graph x, y
grapher.grid(color='black', linestyle='--', linewidth=0.5)
