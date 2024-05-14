import re

# Sample text data
text_data = "Name: John, Age: 30, City: New York"

# Define regular expression pattern
pattern = r"Name: (\w+), Age: (\d+), City: (\w+)"

# Parse text using regular expression
match = re.match(pattern, text_data)

if match:
    print("Name:", match.group(1))
    print("Age:", match.group(2))
    print("City:", match.group(3))
