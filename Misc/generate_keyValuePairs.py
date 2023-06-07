import re
import sys

def return_string_in_double_quotes(string: str):  # using single quotes
    return '"' + string + '"'  # enclosing the string within double quotes


def extract_strings(input_string):
    pattern = r"label:\s+'([^']*)'"
    matches = re.findall(pattern, input_string)
    return matches

def extract_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
    output_string = extract_strings(input_string)
    return output_string


if __name__ == "__main__":
    # Example usage
    file_path = sys.argv[1]
    # file_path = r"C:\vManage\lat_script_pr_2\nms\src\main\client\src-ng2\app\configuration\templates\groups\mini-workflows\feature-profile\profile-parcel\logging-parcel\logging-parcel.constant.ts"
    output = extract_strings_from_file(file_path)
    
    for i in output:
        if i != "":
            print(f"    {return_string_in_double_quotes(i)}: {return_string_in_double_quotes(i)},")


