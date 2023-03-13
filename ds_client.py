"""
Clien module that allows user to upload post or bio
"""
# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import socket
import ds_protocol
import ui
import time


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

        join_msg = ds_protocol.join_txt(username, password)

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

                publish_post = ds_protocol.post_msg(usr_token, message)
                publish_bio = ds_protocol.bio_msg(usr_token, bio)

                send_msg = ds_protocol.direct_msg(usr_token, message, 'ohhimark')

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
                flush_msg(send_, send_msg)
                resp_ = recv.readline()[:-1]
                print("Response received from server: ", resp_)
                flush_msg(send_, send_msg)
                return True
            return True
        except Exception:
            return False


def flush_msg(send_, msg):
    """
    flush data
    """
    send_.write(msg + "\r\n")
    send_.flush()
