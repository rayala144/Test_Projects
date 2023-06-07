import re
import sys

def return_string_in_double_quotes(string: str):  # using single quotes
    return '"' + string + '"'  # enclosing the string within double quotes


def extract_strings(input_string, pattern):
    matches = re.findall(pattern, input_string)
    return matches

def extract_strings_from_file(file_path, regex_pattern):
    with open(file_path, 'r') as file:
        input_string = file.read()
    output_string = extract_strings(input_string, regex_pattern)
    return output_string


if __name__ == "__main__":
    
    file_path = sys.argv[1]    
    output = extract_strings_from_file(file_path, r"label:\s+'([^']*)'")
    
    for i in output:
        if i != "":
            print(f"    {return_string_in_double_quotes(i)}: {return_string_in_double_quotes(i)},")


