import math
pf = float(input("enter the power factor : "))
I = float(input("Enter the current I : "))
V = float(input("Enter the voltage V : "))
P = math.sqrt(3)*pf*I*V
print("Electic current in AC three phase circuit is : ",round(P,3))