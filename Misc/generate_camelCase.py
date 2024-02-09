import json

def camel_case(string: str, max_length=40) -> str:
  """Converts a string to camel case with a maximum length.

  Args:
    string: The string to convert.
    max_length: The maximum length of the output string.

  Returns:
    The string in camel case, truncated if it exceeds max_length.
  """

  words = string.lower().split()
  camel_cased_string = "".join(word.capitalize() for word in words)
  return camel_cased_string[:max_length]


if __name__ == "__main__":

    # Example list of strings
    strings = ["this is a string", "hello world", "another example string"]

    # Create a dictionary with camel-cased strings as keys and original strings as values
    camel_cased_dict = {camel_case(string): string for string in strings}

    # Load the JSON data from a file
    with open(r"C:\TetrationAnalytics\ui\public\locales\en.json", "r") as f:
        json_data = json.load(f)

    # Append the camel-cased dictionary to the JSON data
    json_data.update(camel_cased_dict)

    # Save the modified JSON data back to the file
    with open(r"C:\TetrationAnalytics\ui\public\locales\en.json", "w") as f:
        json.dump(json_data, f, indent=4)

    print("Successfully appended camel-cased dictionary to your_json_file.json!")
