#AUTHOR - Isaac Goff
# DATE - 11/04/2023
# ALGORITHM -
# STEP 1 - Ask user for mode to check percentage plagiarized and file to check
# STEP 2 - Strip and separate input file into map, do same for all files in Files
# STEP 3 - Using maps, find percent of lines with same wording between input file
#          and stored files based on mode, display to user
# STEP 4 - Ask user if they wish to append file into Files folder,
#          ask for rerun or end

# os imported for accessing and moving files outside of directory
import os

# DataStructure imported for splitting, mapping, and comparing of files
import DataStructure

# Sentinel, DataStructure variables made
finished = False
filesep = DataStructure.FileSplitter()

# While loop checks if user has ended program after cycle
while finished is not True:

    # User input determines what files will be marked by system, gets file to check
    mode = input('Enter "p" for total percent of content plagiarized from all files\n'
                 'Enter "q" to check for files with above 25% plagiarized\n'
                 'Enter "h" to check for files with above 50% plagiarized\n'
                 'Enter "t" to check for files with above 75% plagiarized\n'
                 'Enter "f" to check for 100% plagiarism in files\n>    ')
    checkFile = input('Enter name of file to check: ')

    # Input file stripped of tail for name variable, separated for map variable
    checkFileName = checkFile.strip('.txt')
    checkFileRead = filesep.separate(checkFile)

    # Directory variable as all files stored within project
    direc = 'Files/'

    # Lists made for file contents and names respectively
    fileList = []
    fileNames = []

    # For file in Files directory, append name, separate and add to list
    for file in os.listdir('Files/'):
        fileNames.append(file)
        filepath = direc + file
        convertedFile = filesep.separate(filepath)
        fileList.append(convertedFile)

    checkNoPlagiarism = 0

    # For every file and name
    for dict1,fileNames in zip(fileList, fileNames):

        # Try comparing files, check mode to see what files should be marked
        try:
            dict2 = checkFileRead
            result = round(filesep.compare(dict1, dict2) * 100)
            if mode == 'p':
                print(f'{result}% potential plagiarism detected in {checkFileName} matching with {fileNames}')
                checkNoPlagiarism = 1
            elif result >= 25 and mode == 'q':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
                checkNoPlagiarism = 1
            elif result >= 50 and mode == 'h':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
                checkNoPlagiarism = 1
            elif result >= 75 and mode == 't':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
                checkNoPlagiarism = 1
            elif result >= 100 and mode == 'f':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
                checkNoPlagiarism = 1

        # Except Index Error (Incase file empty) continue past error
        except IndexError:
            continue

    if checkNoPlagiarism == 0:
        print(f'Plagiarism not within amount specified for '
              f'{checkFileName} compared to files in database')

    # Ask if user wants to append file to Files directory for future checking
    addfile = input('\nAdd file to files directory for future checking? y/n: ')

    # If yes, add file into directory and tell user, else tell user otherwise
    if addfile.lower() == 'y':
        os.replace(str(checkFile), direc + str(checkFile))
        print(f"{checkFileName} added to Files directory")
    else:
        print(f"{checkFileName} not added")

    # Ask user if they are done, if y, end while loop
    end = input('Finished? y/n:')
    if end.lower() == 'y':
        finished = True
    print()

# Ending statement
print('Thank you for using the Plagiarism Checker\nHave a good day')
