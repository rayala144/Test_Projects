import json
import os
import re
from tkinter import filedialog as fd
from deepdiff import DeepDiff  # This should be imported first using pip install


def getFilePath(fileType):
    # selecting the file using the askopenfilename() method of filedialog
    the_file = fd.askopenfilename(
        title=fileType,
        filetypes=[("json files", "*.json")]
    )
    # getting path of a file using the startfile() method of the os module
    file_path = os.path.abspath(the_file)
    return file_path
    # os.startfile(os.path.abspath(the_file))

try:
    # path to reference json file
    jsn1 = open(getFilePath("Select reference json file"))
    # path to updated/changed json file
    jsn2 = open(getFilePath("Select updated/changed json file"))
except:
    print("File operation interrupted")

# sampleDict = { "name": "Emma", "rollNumber": 5 }
# with open("student.json", "w") as write_file:
#     json.dump(sampleDict, write_file, indent=4)

data1 = json.load(jsn1)
data2 = json.load(jsn2)

result = DeepDiff(data1, data2)
jsoned = json.loads(result.to_json())


keys_added, keys_removed, keys_updated, keys_updated_old = {}, {}, {}, {}

for key in jsoned["dictionary_item_added"]:
    keys_added[(re.findall(r"\'([^\']*)\'", key))[0]] = data2[(re.findall(r"\'([^\']*)\'", key))[0]]

for key in jsoned["dictionary_item_removed"]:
    keys_removed[(re.findall(r"\'([^\']*)\'", key))[0]] = data1[(re.findall(r"\'([^\']*)\'", key))[0]]

for key in jsoned["values_changed"]:
    keys_updated[(re.findall(r"\'([^\']*)\'", key))[0]] = jsoned["values_changed"][key]["new_value"]

for key in jsoned["values_changed"]:
    keys_updated_old[(re.findall(r"\'([^\']*)\'", key))[0]] = jsoned["values_changed"][key]["old_value"]

master_dict = {}
master_dict["keys_added"] = keys_added
master_dict["keys_removed"] = keys_removed
master_dict["keys_updated"] = keys_updated
master_dict["keys_updated_old"] = keys_updated_old   

# print(json.dumps(jsoned, indent=4))

# for key in jsoned.keys():
#     if key == "values_changed":
#         for key1 in jsoned[key].keys():
#             if type(jsoned[key][key1]["new_value"]) is int and type(jsoned[key][key1]["old_value"]) is int:
#                 jsoned[key][key1]["difference"] = abs(jsoned[key][key1]["new_value"] - jsoned[key][key1]["old_value"])
            # print(root)


def ask_choice():
    option = input("Print or save changes.json? ").lower()
    if option == "print" or option == "p":
        print(master_dict)
    elif option == "save" or option == "s":
        with open("changes.json", "w") as outfile:
            json.dump(master_dict, outfile, indent=4)
        print("changes.json file saved")
    else:
        print("Error: Unknown option: " + option + "\nType 'print' or 'p' to print differences and 'save' or 's' to "
                                                   "save the differences as a json file\n")
        ask_choice()



if __name__ == "__main__":
    # ask_choice()
    with open("changes.json", "w") as outfile:
            json.dump(master_dict, outfile, indent=4)
    print("changes.json file saved")
    