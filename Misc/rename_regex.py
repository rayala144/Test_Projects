import re


def replace_pattern_with_trans(match, new_label_pattern):
    label = match.group(1)
    new_label = new_label_pattern.format(label)
    return new_label


def main():
    file_path = r"C:\Users\rakhil\Desktop\Text files\sample.js"

    # Define the old pattern using a regular expression with capturing groups
    old_pattern = r"label: '(.*?)'"

    # Define the new label pattern with a placeholder {label}
    new_label_pattern = "label: <Trans i18nKey='{label}'></Trans>,"

    try:
        # Read the content from the file
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the old pattern with the new pattern using re.sub() with a callback function
        modified_content = re.sub(old_pattern, lambda match: replace_pattern_with_trans(
            match, new_label_pattern), content)

        # Write the modified content back to the file
        with open(file_path, "w") as file:
            file.write(modified_content)

        print("Replacements completed successfully.")
    except IOError:
        print(f"Error: Unable to read or write the file at '{file_path}'.")


if __name__ == "__main__":
    main()
