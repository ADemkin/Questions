'''
This script get all .txt files in folder, get their names and read first line.
Then it prints the first lines of files in list and prompts user to enter which one to choose.
In the end it returns file name of selected element.
'''

import os
import sys



def get_files():
    # create list of all files is /Quiz dir
    files = []
    for file in os.listdir('Quiz'):
        # sort only .txt files
        # ignore all other files like .ds_store
        if os.path.splitext(file)[1] == '.txt':
            files.append(os.path.join('Quiz', file))

    # check if there are any files found
    if len(files) == 0:
        print('There are no quiz files found in /Quiz directory.')
        sys.exit()

    # print a message
    print('Please choose a quiz:')

    # read and print first line of each file
    for i in range(0, len(files)):
        with open(files[i], encoding='ISO-8859-1') as file:
            firstline = file.readline()
            print(i + 1, ': ', firstline, sep='', end='')

    # prompt user for a quiz and return its file name
    s = int(input()) - 1

    # check if correct value entered
    while s not in range(0, len(files)):
        print('Please enter valid quiz number')
        s = int(input()) - 1

    # return file name with extension
    return files[s]


def main():
    print(get_files())


if __name__ == "__main__":
    main()
