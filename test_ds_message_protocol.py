"""
testing the new command of direct
message, retrieve new message, retrieve all message
"""
# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703
import unittest
import ds_protocol
import ds_client


class TestDsProtocol(unittest.TestCase):
    """
    testing the protocol messsage
    """
    def test_dm(self):
        """
        join the server and sending command message
        to ensure receiving ok messaae
        """
        token, send, recv, client = ds_client.only_join('168.235.86.101',
                                                        3021, 'mikey',
                                                        '0123')

        send_msg = ds_protocol.direct_msg(token, 'Hello!', 'ohhimark')
        assert ds_client.flush_and_recv(
            send, send_msg, recv
            ) == {"response": {"type": "ok", "message": "Direct message sent"}}

        find_new = ds_protocol.retrieve_new(token)
        assert ds_client.flush_and_recv(send,
                                        find_new,
                                        recv)["response"]["type"] == "ok"

        find_all = ds_protocol.retrieve_all(token)
        assert ds_client.flush_and_recv(send,
                                        find_all,
                                        recv)["response"]["type"] == "ok"
        client.close()


if __name__ == "__main__":
    unittest.main()
