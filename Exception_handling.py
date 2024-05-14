try:
    # Code that may raise exceptions
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("An error occurred:", e)
