import os
import DataStructure

finished = False
filesep = DataStructure.FileSplitter()
while finished is not True:
    modeDict = {'p': 'Percent Mode', 'q': 'Quarter Mode', 'h': 'Half Mode',
                't': 'Three-Fourths mode', 'f': 'Fully Plagiarised mode'}
    mode = input('Enter "p" for total percent of content plagiarized from all files\n'
                 'Enter "q" to check for files with above 25% plagiarized\n'
                 'Enter "h" to check for files with above 50% plagiarized\n'
                 'Enter "t" to check for files with above 75% plagiarized\n'
                 'Enter "f" to check for 100% plagiarism in files\n>    ')

    checkFile = 'sample-2.txt'
    checkFileName = checkFile.strip('.txt')
    checkFileRead = filesep.separate(checkFile)

    # Directory variable.
    direc = 'Files/'
    fileList = []
    fileNames = []
    for file in os.listdir('Files/'):
        fileNames.append(file)
        filepath = direc + file
        convertedFile = filesep.separate(filepath)
        fileList.append(convertedFile)

    for file in fileList:
        documents = file.values()

    for dict1,fileNames in zip(fileList, fileNames):
        try:
            dict2 = checkFileRead
            result = round(filesep.compare(dict1, dict2) * 100)
            if mode == 'p':
                print(f'{result}% potential plagiarism detected in {checkFileName} matching with {fileNames}')
            elif result >= 25 and mode == 'q':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
            elif result >= 50 and mode == 'h':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
            elif result >= 75 and mode == 't':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
            elif result >= 100 and mode == 'f':
                print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {fileNames}')
            else:
                print(f'Plagiarism not within amount specified for {checkFileName}')
        except IndexError:
            continue




    addfile = input('\nAdd file to files directory for future checking? y/n: ')
    if addfile.lower() == 'y':
        os.replace(str(checkFile), direc + str(checkFile))
        print(f"{checkFileName} added to Files directory")
    else:
        print(f"{checkFileName} not added")

    end = input('Finished? y/n:')
    if end.lower() == 'y':
        finished = True
    print()




print('Thank you for using the Plagiarism Checker\nHave a good day')