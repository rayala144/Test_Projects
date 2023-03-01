import os
import re
from tkinter import filedialog as fd
# Store the current directory
CUR_DIR = fd.askdirectory()

# Search for every file inside this directory
allFiles = os.listdir(CUR_DIR)

# Iterate over each and every file
for file in allFiles:

    if file.endswith('.json'):
        # Read the entire contents of that file
        textToBeSearched = open(file).read()

        # Create a regex pattern to find strings within all code blocks
        stringRegexPattern_1 = r"i18n.t\(\x27([a-z 0-9_]*)\x27\)"  # for i18n.t('key')
        stringRegexPattern_2 = r" t\(\x27([a-z 0-9_]*)\x27\)"  # for t('key')
        stringRegexPattern_3 = r" i18nKey='([^']*)'"
        patterns = [stringRegexPattern_1, stringRegexPattern_2, stringRegexPattern_3]
        


        # Apply this regex pattern on the content of the file
        master_wordList = [re.findall(pattern, textToBeSearched) for pattern in patterns]

        # Print out the list of words
        print(master_wordList)

# if __name__ == '__main__':
#     print(wordsList)
