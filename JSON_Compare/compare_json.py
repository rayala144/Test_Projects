import json
from deepdiff import DeepDiff


# path to reference json file
jsn1 = open('./JSON_Compare/sample1.json')
# path to updated/changed json file
jsn2 = open('./JSON_Compare/sample2.json')

# sampleDict = { "name": "Emma", "rollNumber": 5 }
# with open("student.json", "w") as write_file:
#     json.dump(sampleDict, write_file, indent=4)

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



def ask_choice():
    option = input("Print or save compare.json? ").lower()
    if option == "print" or option == "p":
        print(jsoned)
    elif option == "save" or option == "s":
        with open("compare.json", "w") as outfile:
            json.dump(jsoned, outfile, indent=4)
        print("compare.json file saved")
    else:
        print("Error: Unknown option: " + option + "\nType 'print' or 'p' to print differences and 'save' or 's' to save the differences as a json file\n")
        ask_choice()


if __name__ == "__main__":
    ask_choice()


