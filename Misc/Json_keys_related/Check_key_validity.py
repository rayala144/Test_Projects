import json
import os
from tkinter import filedialog as fd


def getFilePath():
    # selecting the file using the askopenfilename() method of filedialog
    the_file = fd.askopenfilename(
        title="Select a json file",
        filetypes=[("Json files", "*.json")]
    )
    # getting path of a file using the startfile() method of the os module
    file_path = os.path.abspath(the_file)
    return file_path
    # os.startfile(os.path.abspath(the_file))


def filter_json_keys(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)

    filtered_keys = {}
    for key in data.keys():
        if len(key) >= 70 or cap_check(key):
            filtered_keys[key] = data[key]

    return filtered_keys


def cap_check(key: str):
    # a=[segment[0].isupper() for segment in key.split('.')]
    a = key.split('.')
    for segment in a:
        if segment:
            if segment[0].isupper() is True or (not segment.isalnum()):
                return True


if __name__ == "__main__":
    # Replace 'your_file.json' with the actual path to your JSON file
    json_file_path = getFilePath()
    filtered_keys = filter_json_keys(json_file_path)
    print(len(filtered_keys))

    with open("Misc\Json_keys_related\invalid_keys.json", 'w') as file:
        # file.write("Filtered keys:\n")
        # for key in filtered_keys:
        #     file.write(f'"{key}"\n')
        json.dump(filtered_keys, file, indent=4)

    print("Filtered Keys:\n\n")
    for key in filtered_keys:
        print(key)
