import math

# Input number of terms for the sine series
num_terms = int(input("Enter the number of terms for the sine series: "))

# Initialize sum of the series
total_sum = 0

# Compute the sum of the sine series
for i in range(1, num_terms + 1):
    term = math.sin(i)
    total_sum += term

# Display the sum of the sine series
print("Sum of the sine series:", total_sum)
