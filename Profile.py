"""
Profile module
"""
# Profile.py
#
# ICS 32
#
# Author: Mark S. Baldwin, modified by Alberto Krone-Martins
#
# v0.1.9

#
# YOU DO NOT NEED TO READ OR UNDERSTAND THE JSON SERIALIZATION ASPECTS OF THIS
# CODE
# RIGHT NOW, though can you certainly take a look at it if you are curious
# since we already covered a bit of the JSON format in class.
#
import json
from pathlib import Path
import ds_messenger


class DsuFileError(Exception):
    """
    DsuFileError is a custom exception handler that you should catch in your
    owncode. It is raised when attempting to load or save Profile objects to
    file the system.
    """


class DsuProfileError(Exception):
    """
    DsuProfileError is a custom exception handler that you should catch in your
    own code. It is raised when attempting to deserialize a dsu file to a
    Profile object.
    """


class Profile:
    """
    The Profile class exposes the properties required to join an ICS 32 DSU
    server. You will need to use this class to manage the information provided
    by each new user created within your program for a2. Pay close attention to
    the properties and functions in this class as you will need to make use of
    each of them in your program.

    When creating your program you will need to collect user input for the
    properties exposed by this class. A Profile class should ensure that a
    username and password are set, but contains no conventions to do so. You
    should make sure that your code verifies that required properties are set.
    """

    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver  # REQUIRED
        self.username = username  # REQUIRED
        self.password = password  # REQUIRED
        self._friend = []
        self._messages = []

    def save_profile(self, path: str) -> None:
        """
        save profile information
        """
        _path = Path(path)

        if _path.exists() and _path.suffix == '.dsu':
            try:
                _file = open(_path, 'w', encoding='utf-8')
                json.dump(self.__dict__, _file)
                _file.close()
            except Exception as ex:
                raise DsuFileError("Error while attempting to process the\
                 DSU file.", ex) from ex
        else:
            raise DsuFileError("Invalid DSU file path or type")
        return True

    def load_profile(self, path: str) -> None:
        """
        get profile
        """
        path_ = Path(path)

        if path_.exists() and path_.suffix == '.dsu':
            try:
                file = open(path_, 'r', encoding='utf-8')
                obj = json.load(file)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self._friend = obj["_friend"]
                for dir_msg_obj in obj["_messages"]:
                    msg = ds_messenger.DirectMessage()
                    msg.set_attributes(dir_msg_obj["message"],
                                       dir_msg_obj["recipient"],
                                       dir_msg_obj["timestamp"])
                    self._messages.append(msg)
                file.close()
            except Exception as ex:
                raise DsuProfileError(ex) from ex
        else:
            raise DsuFileError()
        return True
