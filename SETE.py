import os
while True:
    mode = input('SETE> ')
    if mode == 'nf':
        newFile_name = input('FILE NAME> ')
        with open(newFile_name, 'w') as file:
            file.write(input('ENTER CONTENT> '))
    elif mode == 'of':
        openedFile_name = input('FILE NAME> ')
        with open(openedFile_name, 'a') as file:
            file.write('\n')
            file.write(input('ENTER CONTENT> '))
    elif mode == 'ep':
        input('Press enter to exit')
        exit()
    elif mode == 'Subscribe to SyntaxError':
        print('based')
    elif mode == 'rp':
        print('Run a program by typing its file location in the terminal(macos, linux) or command prompt(windows)')
    elif mode == 'ofml5':
        openedFile_name = input('FILE NAME> ')
        with open(openedFile_name, 'a') as file:
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 1> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 2> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 3> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 4> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 5> '))
    
    elif mode == 'ofml15':
        openedFile_name = input('FILE NAME> ')
        with open(openedFile_name, 'a') as file:
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 1> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 2> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 3> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 4> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 5> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 6> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 7> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 8> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 9> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 10> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 11> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 12> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 13> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 14> '))
            file.write('\n')
            file.write(input('ENTER CONTENT LINE 15> '))
    elif mode == 'fr':
        readFile_name = input('FILE NAME> ')
        readFile_content = open(readFile_name, 'r')
        print('Contents of: ', readFile_name, '\n\n\n', readFile_content.read())
    elif mode == 'si':
        print('======== Software Information ========')
        print('==== Created by SyntaxError52')
        print('==== v1.1')
    elif mode == 'uh':
        print('======================== Help ========================')
        print('====== SETE is a modal editor')
        print('====== You type in letters to change your actions')
        print('====== Here is a list')
        print('====== - nf, New File')
        print('====== - of, Write a line of code in a file')
        print('====== - ep, Exit Program')
        print('====== - ofml5, Write 5 lines of code in a file')
        print('====== - fr, Read a file')
        print('====== - uh, This! (user help)')
        print('====== - rp, Information on how to run a program')
        print('====== - si, software informaition')
    else:
        print('You Dingus, type uh')
