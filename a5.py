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
import ds_client
import Profile
import ui
from OpenWeather import OpenWeather
from LastFM import LastFm


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
    elif input_command[0] == 'P':
        p_command(saved_file)
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


def o_command() -> str:
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
                new_transclude_entry = check_keyword(entry)
                if entry.isspace():
                    print('post cannot be empty')
                else:
                    new_post = Profile.Post(new_transclude_entry)
                    profile.add_post(new_post)
                    ds_client.send(
                        profile.dsuserver,
                        3021,
                        profile.username, profile.password,
                        new_transclude_entry, profile.bio)
            elif _str == '-delpost':
                _id = input_command[input_command.index('-delpost') + 1]
                profile.get_posts()
                profile.del_post(int(_id))
        profile.save_profile(dsu_file)


def p_command(saved_file):
    """
    Command P (printing)
    """
    if saved_file:
        dsu_file = saved_file
        print(f"The dsu file that is obtained is {str(dsu_file)}")
        profile = Profile.Profile()
        print(profile)
        profile.load_profile(dsu_file)
        for _str in input_command:
            if _str == '-usr':
                print(profile.username)
            elif _str == '-pwd':
                print(profile.password)
            elif _str == '-bio':
                print(profile.bio)
            elif _str == '-posts':
                all_post = profile.get_posts()
                for post in all_post:
                    print(f'id:{all_post.index(post)} post:{post}')
            elif _str == '-post':
                id_ = input_command[input_command.index('-post') + 1]
                print(profile.get_posts()[int(id_)])
            elif _str == '-all':
                print(f'dsuserver: {profile.dsuserver}')
                print(f'username: {profile.username}')
                print(f'password: {profile.password}')
                print(f'bio: {profile.bio}')
                print(f'posts: {profile.get_posts()}')


def weather_transcluded(entry):
    """
    transclusion for openweather class
    """
    ccode = 'US'
    zipcode = '92697'
    apikey = "bb34f51838f49bca2be3d07c1285afa1"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    transcluded_entry = entry.split()
    for element in enumerate(transcluded_entry):
        if transcluded_entry[element[0]] == '@weather':
            transcluded_entry[element[0]] = open_weather.transclude(
                message=transcluded_entry[element[0]])

    return ' '.join(transcluded_entry)


def lastfm_transcluded(entry):
    """
    transclusion for lastfm class
    """
    artist = 'keshi'
    album = 'GABRIEL'
    apikey = "805379ee63e55d5dba6a123ab70e48f5"

    last_fm = LastFm(artist, album)
    last_fm.set_apikey(apikey)
    last_fm.load_data()

    new_entry = entry.split()
    for element in enumerate(new_entry):
        if new_entry[element[0]] == '@lastfm':
            new_entry[element[0]] = last_fm.transclude(
                message=new_entry[element[0]])

    return ' '.join(new_entry)


def check_keyword(entry):
    """
    Check if keyword is in the post entered
    """
    transclude_post = entry
    if '@lastfm' in entry and '@weather' in entry:
        transclude_post = lastfm_transcluded(weather_transcluded(entry))
    else:
        if '@lastfm' in entry:
            transclude_post = lastfm_transcluded(entry)
        elif '@weather' in entry:
            transclude_post = weather_transcluded(entry)
        else:
            pass
    return transclude_post


if __name__ == "__main__":
    SAVED_FILE = None

    while True:
        command = ui.enter_ui()
        try:
            input_command = command  # ui

            if input_command[0] in ["L", "O", "C", "D", "R"]:
                inputPath = Path(input_command[1])

            if len(input_command) >= 2:
                SAVED_FILE = main(SAVED_FILE)
        except (FileNotFoundError, IndexError, TypeError) as e:
            print(e)
