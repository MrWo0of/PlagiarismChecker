import os
from difflib import SequenceMatcher
finished = False
while finished is not True:
    modeDict = {'p': 'Percent Mode', 'q': 'Quarter Mode', 'h': 'Half Mode',
                't': 'Three-Fourths mode', 'f': 'Fully Plagiarised mode'}
    mode = input('Enter "p" for total percent of content plagiarized from all files\n'
                 'Enter "q" to check for files with above 25% plagiarized\n'
                 'Enter "h" to check for files with above 50% plagiarized\n'
                 'Enter "t" to check for files with above 75% plagiarized\n'
                 'Enter "f" to check for 100% plagiarism in files\n>    ')

    # Directory variable.
    direc = 'Files/'
    fileList = [direc + f for f in os.listdir(direc) if f.endswith('.txt')]
    checkFile = input('Enter the file\'s name to check for plagiarism: ')
    checkFileName = checkFile.strip('.txt')
    checkFileOpen = open(checkFile, 'r')
    checkFileRead = checkFileOpen.read()


    documents = [open(f).read() for f in fileList]


    for filename, document in zip(fileList, documents):
        ab = SequenceMatcher(None, document, checkFileRead).ratio()
        result = int(ab * 100)
        if mode == 'p':
            print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')
        elif result >= 25 and mode == 'q':
            print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')
        elif result >= 50 and mode == 'h':
            print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')
        elif result >= 75 and mode == 't':
            print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')
        elif result >= 100 and mode == 'f':
            print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')
        else:
            print(f'Plagiarism not within amount specified for {checkFileName}')

    checkFileOpen.close()

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