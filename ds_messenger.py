# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703
import ds_client
import ds_protocol
import socket


class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.server = dsuserver
        self.username = username
        self.password = password

    def send(self, message: str, recipient: str) -> bool:
        # must return true if message successfully sent, false if send failed.
        self.token, send, recv = ds_client.only_join(self.server, 3021, self.username, self.password)
        send_msg = ds_protocol.direct_msg(self.token, message, recipient)
        if ds_client.flush_and_recv(send, send_msg, recv):
            return True
        return False


    def retrieve_new(self) -> list:
        # must return a list of DirectMessage objects containing all new messages
        pass

    def retrieve_all(self) -> list:
        # must return a list of DirectMessage objects containing all messages
        pass

def run():
    direct_msgr = DirectMessenger()