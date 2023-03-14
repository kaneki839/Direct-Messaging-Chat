"""
protols that ensure the formatting issue
"""
# ds_protocol.py

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import json
import time
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['response', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to a
    DataTuple object

    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        token = json_obj['response']['token']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(response, token)


def to_json(dict_):
    """
    conver dictionary to json format
    """
    json_str = json.dumps(dict_)
    return json_str


def from_json(json_msg):
    p_dict = json.loads(json_msg)
    return p_dict


def bio_msg(token, _bio):
    """
    formatting bio
    """
    dict_bio = {"token": f"{token}", "bio": {"entry": f"{_bio}", "timestamp":
                                             f"{time.time()}"}}
    bio_text = to_json(dict_bio)
    return bio_text


def post_msg(token, _post):
    """
    formatting post
    """
    dict_post = {"token": f"{token}", "post": {"entry": f"{_post}",
                                               "timestamp": f"{time.time()}"}}
    post_ = to_json(dict_post)
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


def direct_msg(_token, send_msg, recipent):
    """
    formatting direct message
    """
    dict_msg = {"token": f"{_token}",
                "directmessage": {"entry": f"{send_msg}",
                                  "recipient": f"{recipent}",
                                  "timestamp": f"{time.time()}"}}
    msg_ = to_json(dict_msg)
    return msg_


def retrieve_new(_token):
    """
    formatting retrieve of new message
    """
    unread_msg = {"token": f"{_token}", "directmessage": "new"}
    unread = to_json(unread_msg)
    return unread


def retrieve_all(_token):
    """
    formatting retrieve of all messages
    """
    all_msg = {"token": f"{_token}", "directmessage": "all"}
    all = to_json(all_msg)
    return all
