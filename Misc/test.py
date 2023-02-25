import os
from tkinter import filedialog as fd


def getFilePath():
    # selecting the file using the askopenfilename() method of filedialog
    the_file = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("All files", "*.*")]
    )
    # getting path of a file using the startfile() method of the os module
    file_path = os.path.abspath(the_file)
    return file_path
    # os.startfile(os.path.abspath(the_file))


if __name__ == "__main__":
    print(getFilePath())
