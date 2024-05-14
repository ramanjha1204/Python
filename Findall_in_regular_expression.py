import re 
pattern = r"[a-z A-Z]+\d+"
matches = re.findall(pattern," LXI 2012,VI 2015")
for match in matches:
    print(match,end= "")