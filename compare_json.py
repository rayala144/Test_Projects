import json
from deepdiff import DeepDiff


# path to json file
jsn1 = open('HCL Assignments\Project assignment\sample_1.json')
# path to json file
jsn2 = open('HCL Assignments\Project assignment\sample_2.json')

data1 = json.load(jsn1)
data2 = json.load(jsn2)

result = DeepDiff(data1, data2)
jsoned = json.loads(result.to_json())

# print(json.dumps(jsoned, indent=4))

for key in jsoned.keys():
    if key == "values_changed":
        for key1 in jsoned[key].keys():
            if type(jsoned[key][key1]["new_value"]) is int and type(jsoned[key][key1]["old_value"]) is int:
                jsoned[key][key1]["difference"] = abs(jsoned[key][key1]["new_value"] - jsoned[key][key1]["old_value"])
            # print(root)


option = input("Print or save? ").lower()

if option == "print":
    print(jsoned)
elif option == "save":
    with open("compare.json", "w") as outfile:
        json.dump(jsoned, outfile, indent=4)
    print("compare.json saved")
else:
    print("Error: Unknown option: " + option)

# sampleDict = { "name": "Emma", "rollNumber": 5 }
# with open("student.json", "w") as write_file:
#     json.dump(sampleDict, write_file, indent=4)
