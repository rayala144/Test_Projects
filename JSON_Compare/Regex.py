import re

string = "root['stamina']"
result = (re.findall(r"\'([^\']*)\'", string))[0]
print(result)  # will return the string 'stamina' 
