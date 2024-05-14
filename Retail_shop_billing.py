# retail shop billing 
item = input("Enter product name : ")
unit_price = float(input("Enter product price : "))
quantity = int(input("Enter quantity : "))

cost = unit_price * quantity
print("total cost : ", cost)
payment = float(input("enter cash paid :"))
change = payment - cost
print("billing amount :", cost)
print("amount paid : ", payment)
print(" pay change : ", change)