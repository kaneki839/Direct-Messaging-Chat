"""
Clien module that allows user to upload post or bio
"""
# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import socket
import time
import ds_protocol
import ui


def send(
        server: str,
        port: int, username: str, password: str, message: str, bio: str = None
        ):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))

        print(f'Client connected to {server} on {port}')

        join_msg = join_txt(username, password)

        send_ = client.makefile('w')
        recv = client.makefile('r')

        try:
            join, post, _bio_ = ui.send_process()
            if join:
                flush_msg(send_, join_msg)
                resp = recv.readline()[:-1]
                print("Response received from server: ", resp)
                data_tuple = ds_protocol.extract_json(resp)
                usr_token = data_tuple.token

                publish_post = post_msg(usr_token, message)
                publish_bio = bio_msg(usr_token, bio)

                if post and (not _bio_):
                    flush_msg(send_, publish_post)
                    print('Post successfuly uploaded')
                elif _bio_ and (not post):
                    flush_msg(send_, publish_bio)
                    print('Bio successfully uploaded')
                elif post and _bio_:
                    flush_msg(send_, publish_post)
                    time.sleep(0.1)
                    flush_msg(send_, publish_bio)
                    print('Post and Bio successfully uploaded')
                else:
                    pass
                return True
            return True
        except Exception:
            return False


def bio_msg(token, _bio):
    """
    formatting bio
    """
    dict_bio = {"token": f"{token}", "bio": {"entry": f"{_bio}", "timestamp":
                                             f"{time.time()}"}}
    bio_text = ds_protocol.to_json(dict_bio)
    return bio_text


def post_msg(token, _post):
    """
    formatting post
    """
    dict_post = {"token": f"{token}", "post": {"entry": f"{_post}",
                                               "timestamp": f"{time.time()}"}}
    post_ = ds_protocol.to_json(dict_post)
    return post_


def join_txt(username, password):
    """
    formatting join
    """
    usr = f'"username": "{username}"'
    psw = f'"password": "{password}"'
    info_txt = f'{{{usr}, {psw}, "token":""}}'

    join = f'"join": {info_txt}'
    join_msg = '{' + join + '}'
    return join_msg


def flush_msg(send_, msg):
    """
    flush data
    """
    send_.write(msg + "\r\n")
    send_.flush()
