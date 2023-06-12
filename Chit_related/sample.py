import re
string = "RK 1,2,2,4,7,9,11,12, 13,14,15,16,18,19,20,21,25,26"
string_1 = re.findall(r'\d+', string)
# string_1 = string.strip().split(" ")[-1].split(",")
print(string_1)