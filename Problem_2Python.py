from math import sqrt

def Circle(a1, b1, a2, b2, a3, b3):
        
        a12 = a1 - a2;
        a13 = a1 - a3;
        a31 = a3 - a1;
        a21 = a2 - a1;
        
        b12 = b1 - b2;
        b13 = b1 - b3;
        b31 = b3 - b1;
        b21 = b2 - b1;
        
        # solve for Xx, Yy, Z
        w = pow(a1, 2) - pow(a3, 2);
        x = pow(b1, 2) - pow(b3, 2);
        y = pow(a2, 2) - pow(a1, 2);
        z = pow(b2, 2) - pow(b1, 2);
        
        d = (((w) * (a12) + (x) * (a12) + (y) * (a13) + (z) * (a13)) // (2 * ((b31) * (a12) - (b21) * (a13))));
        e = (((w) * (b12) + (x) * (b12) + (y) * (b13) + (z) * (b13)) // (2 * ((a31) * (b12) - (a21) * (b13))));
        c = (-pow(a1, 2) - pow(b1, 2) - 2 * e * a1 - 2 * d * b1);
        
        h = -e;
        k = -d;
        print("Centre = (", h, ", ", k, ")"); # print the center coordinates
        
        r_sqrt = h*h+k*k-c;
        r = round(sqrt(r_sqrt), 5);
        print("Radius = ", r);   # print the radius
        
        l=[2*e,2*d,c]
        print("vector[D,E,F]",l) # print the vector
        
# Input 3 Coordinates
a1,b1 = map(int,input('Input the First Coordinates: ').split()) 
a2,b2 = map(int,input('Input the Second Coordinates: ').split())
a3,b3 = map(int,input('Input the Third Coordinates: ').split())
Circle(a1, b1, a2, b2, a3, b3)