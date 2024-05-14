# python program to calculate the weight of a motorbike
engine_weight = float(input("Enter the weight of the engine (in kg): "))
frame_weight = float(input("Enter the weight of the frame (in kg): "))
wheel_weight = float(input("Enter the weight of a wheel (in kg): "))
total_weight = engine_weight + frame_weight + 2 * wheel_weight
print("Total weight of the motorbike:", total_weight, "kg")