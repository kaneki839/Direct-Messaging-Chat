"""
Main module that run whole program
"""
# a5.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

from pathlib import Path
import sys
import Profile
import ui
import ds_messenger


def main(saved_file=None):
    """
    Function contain command that don't need recursive search
    """
    if input_command[0] == 'Q':
        sys.exit('Quit')
    elif input_command[0] == 'C':
        saved_file = c_command()
    elif input_command[0] == 'O':
        saved_file = o_command()
    elif input_command[0] == 'E':
        e_command(saved_file)
    return saved_file


def c_command():
    """
    Command C (create a dsu file with user specified name)
    """
    if len(input_command) == 4 and input_command[2] == '-n':
        mypath = Path(f'{input_command[1]}/{input_command[3]}.dsu')
        if mypath.exists():
            profile = Profile.Profile()
            profile.load_profile(str(mypath))
            print('File already exist, the file loaded')
        else:
            print('server address:')
            server_address = input()
            print('username: ')
            name = input()
            print('password: ')
            psw = input()
            if (name.find(" ") == -1) or (psw.find(" ") == -1):
                print('bio: ')
                bio = input()
                mypath.touch()
                profile = Profile.Profile(username=name, password=psw)
                profile.dsuserver = server_address
                if bio.isspace():
                    print('bio cannot be empty')
                else:
                    profile.bio = bio
                    profile.save_profile(mypath)
                    print(f"{mypath.name} has been successfully created!")
            else:
                print("You cannot have a whitespace in your name or password.")
        saved_file = str(mypath)
        return saved_file
    print('ERROR')
    return None


def o_command():
    """
    Command O (load the entered dsu file)
    """
    if '.dsu' in str(inputPath):
        if inputPath.exists():
            profile = Profile.Profile()
            profile.load_profile(inputPath)
            saved_file = inputPath
            print(f"The file {saved_file} is opened and set!")
            return str(saved_file)
        print('ERROR, File does not exist')
        return None
    print(f'ERROR. Unable to open file {inputPath}')
    return None


def e_command(saved_file):
    """
    Command E (editing)
    """
    if saved_file:
        dsu_file = saved_file
        print(f"The dsu file that is obtained is {str(dsu_file)}")
        profile = Profile.Profile()
        profile.load_profile(dsu_file)
        command_ = input_command
        all_option = ['-usr', '-pwd', '-bio', '-addpost', '-delpost']

        # check comand
        for element in enumerate(input_command):
            if element[0] % 2 == 1:
                if input_command[element[0]] not in all_option:
                    print('ERROR')
                    break

        for _str in input_command:
            if _str == '-usr':
                profile.username = command_[command_.index('-usr') + 1]
            elif _str == '-pwd':
                profile.password = command_[command_.index('-pwd') + 1]
            elif _str == '-bio':
                profile.bio = input_command[input_command.index('-bio') + 1]
            elif _str == '-addpost':
                entry = input_command[input_command.index('-addpost') + 1]
                if entry.isspace():
                    print('post cannot be empty')
                else:
                    new_post = Profile.Post(entry)
                    profile.add_post(new_post)

                    # a5 stuff
                    sender_obj = ds_messenger.DirectMessenger('168.235.86.101', 'killua', '789')
                    recipient = 'ohhimark'
                    msg = 'test_msg'
                    sender_obj.send(msg, recipient)
                    profile.add_recipient(recipient)
                    sender_lst = sender_obj.retrieve_all()
                    for dsm_obj in sender_lst:
                        msg_dict = dsm_obj.__dict__
                        profile.add_msg(msg_dict)
            elif _str == '-delpost':
                _id = input_command[input_command.index('-delpost') + 1]
                profile.get_posts()
                profile.del_post(int(_id))
        profile.save_profile(dsu_file)


if __name__ == "__main__":
    SAVED_FILE = None

    while True:
        command = ui.enter_ui()
        try:
            input_command = command  # ui

            if input_command[0] in ["O", "C"]:
                inputPath = Path(input_command[1])

            if len(input_command) >= 2:
                SAVED_FILE = main(SAVED_FILE)
        except (FileNotFoundError, IndexError, TypeError) as e:
            print(e)
