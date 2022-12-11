import os
from Password_Generator import generate


def rename():
    i = 1
    path = input("Enter the path of the folder: ")
    new_name = input("What do you want to rename with? ")
    extension = input("Which format? ")
    for filename in os.listdir(path):
        my_dest = new_name + ' ' + str(i) + '.' + extension
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == '__main__':
    password = generate(5)
    print(password)