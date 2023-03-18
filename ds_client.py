"""
Clien module that allows user to upload post or bio
"""
# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import socket
import ds_protocol


def only_join(server: str, port: int, username: str, password: str):
    """
    join the server and acquire user token
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server, port))
    print(f'Client connected to {server} on {port}')

    send_ = client.makefile('w')
    recv = client.makefile('r')

    join_msg = ds_protocol.join_txt(username, password)
    flush_msg(send_, join_msg)
    resp = recv.readline()[:-1]
    print("Response received from server: ", resp)
    data_tuple = ds_protocol.extract_json(resp)
    usr_token = data_tuple.token

    return usr_token, send_, recv, client


def flush_msg(send_, msg):
    """
    flush data
    """
    send_.write(msg + "\r\n")
    send_.flush()


def flush_and_recv(send_, msg, recv_):
    """
    flushing and printing the response
    """
    send_.write(msg + "\r\n")
    send_.flush()
    resp = recv_.readline()[:-1]
    print("Response received from server: ", resp)
    return ds_protocol.from_json(resp)
