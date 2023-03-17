"""
module that process three commands including direct
message, retrieve unread message, and retrieve all message
"""
import ds_client
import ds_protocol


class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    """
    class that contain three methods to execute different commands
    """
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password

    def send(self, message: str, recipient: str) -> bool:
        """
        method for direct message
        """
        # must return true if message successfully sent, false if send failed.
        self.token, send, recv, \
            client = ds_client.only_join(self.dsuserver, 3021,
                                         self.username, self.password)
        send_msg = ds_protocol.direct_msg(self.token, message, recipient)
        resp = ds_client.flush_and_recv(send, send_msg, recv)
        client.close()
        if resp["response"]["type"] == "ok":
            return True
        return False

    def retrieve_new(self) -> list:
        """
        method for retrieving new message
        """
        # must return a list of DirectMessage objects containing all new
        # messages
        self.token, send, recv, \
            client = ds_client.only_join(self.dsuserver, 3021,
                                         self.username, self.password)
        unread_req = ds_protocol.retrieve_new(self.token)
        resp = ds_client.flush_and_recv(send, unread_req, recv)
        client.close()
        msg_lst = resp["response"]["messages"]
        dm_lst = []
        for msg in msg_lst:
            dm_obj = DirectMessage()
            dm_obj.recipient = self.username
            dm_obj.message = msg["message"]
            dm_obj.timestamp = msg["timestamp"]
            dm_lst.append(dm_obj)
        return dm_lst

    def retrieve_all(self) -> list:
        """
        method for retrieving all messages
        """
        # must return a list of DirectMessage objects containing all messages
        self.token, send, recv, \
            client = ds_client.only_join(self.dsuserver, 3021,
                                         self.username, self.password)
        all_req = ds_protocol.retrieve_all(self.token)
        resp = ds_client.flush_and_recv(send, all_req, recv)
        client.close()
        msg_lst = resp["response"]["messages"]
        dm_lst = []
        for msg in msg_lst:
            dm_obj = DirectMessage()
            dm_obj.recipient = self.username
            dm_obj.message = msg["message"]
            dm_obj.timestamp = msg["timestamp"]
            dm_lst.append(dm_obj)
        return dm_lst


sender_obj = DirectMessenger('168.235.86.101', 'mikey', '0123')
sender_obj.send('testing again', 'mikey')
print(sender_obj.retrieve_new())
print(sender_obj.retrieve_all())
