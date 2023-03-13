"""
User interface
"""
# ui.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import sys


def command_menu():
    """
    Menu of all commands
    """
    command_lst = []
    print()
    print('------------- Welcome! ---------------')
    print('Enter the following command:\n')
    print('L (Observe the content in directory)')
    print('C (Create a dsu file)')
    print('D (Delete the file)')
    print('R (Read the content of the file)')
    print('O (Load the file)')
    print('E (Edit the file [Must execute C or O in advance])')
    print('P (Get data stored in the file [Must execute C or O in advance])')
    print('Q (Quit)')
    print('---------------------------------------')
    command = input()
    command_lst.append(command)
    return command_lst


def join_server():
    """
    Check if user want join server
    """
    ask = input('Do you want join the DSP server? (Y/N) ')
    if ask == 'Y':
        return True
    if ask == 'N':
        return False
    sys.exit('Invalid command')


def upload_bio():
    """
    Check if user want upload bio
    """
    bio_ask = input('Do you want to upload bio? (Y/N) ')
    if bio_ask == 'Y':
        return True
    if bio_ask == 'N':
        return False
    sys.exit('Invalid command')


def upload_post():
    """
    Check if user want upload post
    """
    post_ask = input('Do you want to upload post? (Y/N) ')
    if post_ask == 'Y':
        return True
    if post_ask == 'N':
        return False
    sys.exit('Invalid command')


def send_process():
    """
    Checking system for client module
    """
    join = False
    if join_server():
        join = True
        post = upload_post()
        bio = upload_bio()
        return join, post, bio
    return None


def enter_ui():
    """
    Whole user interface for a4 module
    """
    command_lst = command_menu()
    if command_lst[0] in ['L', 'C', 'D', 'R', 'O']:
        print('Great! What is the name of the file? (Path)')
        path = input()
        command_lst.append(path)
        if command_lst[0] == 'L':
            print('Enter the option you wanna execute for L command):')
            print('[whitespace] (get contents in the directory)')
            print('-r (output directory content recursively)')
            print('-f (Output only files)')
            print('-s Output only files correspond to given file name')
            print('-e Output only files correspond to given file extension')
            print('OR combo option: "-r -f" "-r -s" "-r -e"')
            option = input()
            if option.isspace():
                pass
            else:
                option = option.split(' ')
                command_lst = command_lst + option
            if '-s' in option:
                print('Enter the file name:')
                file_name = input()
                command_lst.append(file_name)
            elif '-e' in option:
                print('Enter the file extension:')
                extension = input()
                command_lst.append(extension)
        elif command_lst[0] == 'C':
            print('Add -n to specify the name of file you want to created')
            _specifier = input()
            command_lst.append(_specifier)
            print('Enter the name of the file you want to created:')
            name = input()
            command_lst.append(name)
    elif command_lst[0] in ['E', 'P']:
        if command_lst[0] == 'E':
            print()
            print('Enter the option you want to execute:')
            print('-usr (username)\n-pwd (password)\n-bio (bio)')
            print('-addpost (new post)')
            print('-delpost (delete post)')
            feature = input()
            command_lst.append(feature)
            if feature == '-usr':
                print('Enter the username:')
                usr = input()
                command_lst.append(usr)
            elif feature == '-pwd':
                print('Enter the password:')
                pwd = input()
                command_lst.append(pwd)
            elif feature == '-bio':
                print('Enter the bio:')
                bio = input()
                command_lst.append(bio)
            elif feature == '-addpost':
                print('Enter the post:')
                print('You can also enter keyword in your post: ')
                print('@weather (Weather\'s description) / ', end='')
                print('@lastfm (Artist\'s name)')
                post = input()
                command_lst.append(post)
            elif feature == '-delpost':
                print('Enter the id of post you want to delete:')
                id_ = input()
                command_lst.append(id_)
        elif command_lst[0] == 'P':
            print()
            print('Enter the option you want to execute:')
            print('-usr (username)\n-pwd (password)\n-bio (bio)')
            print('-posts (all posts)')
            print('-post (post specified by id)')
            print('-all (all contents in the file)')
            option = input()
            command_lst.append(option)
            if option == '-post':
                print('Enter the id of the post you want to see:')
                id_ = input()
                command_lst.append(id_)
    elif command_lst[0] == 'Q':
        sys.exit('Quit')
    else:
        print('invalid command')

    return command_lst
