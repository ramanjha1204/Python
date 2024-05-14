dia = int(input("enter the diameter of steel bar in milimeter :"))
length = int(input("enter the length of steel bar in meter :"))
weight = ((dia**2)/162)*length
print("weigth of the steel bar in kg per meter :", round (weight,2))