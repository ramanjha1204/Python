import re
strings = ["apple", "banana", "cherry"]
number = 123
pattern = r"^(.*)$"
modified_strings = [re.sub(pattern, r"{}\1".format(number), s) for s in strings]
for s in modified_strings:
    print(s)
