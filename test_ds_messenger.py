"""
testing module that test the ds_messenger module
"""
import time
import unittest
import ds_messenger


class TestDsMessenger(unittest.TestCase):
    """
    class that test all of ds_messenger functionality
    """
    def test_ds_messenger(self):
        """
        first test if direct message was send, then check if the
        retrieve related function return a list that contain all
        the object that's in DirectMessage type
        """
        sender_obj = ds_messenger.DirectMessenger('168.235.86.101',
                                                  'killua', '789')
        assert sender_obj.send('testing again', 'ohhimark') is True
        assert sender_obj.send('None', None) is False

        # assert sender_obj.send('testing again', 2) is False

        assert sender_obj.retrieve_new() == []

        for obj in sender_obj.retrieve_all():
            assert isinstance(obj, ds_messenger.DirectMessage)

    def test_if_new_msg(self):
        sender_obj = ds_messenger.DirectMessenger('168.235.86.101',
                                                  'killua', '789')
        sender_obj.send('testing again', 'killua')
        for obj in sender_obj.retrieve_new():
            assert isinstance(obj, ds_messenger.DirectMessage)
        for obj in sender_obj.retrieve_all():
            assert isinstance(obj, ds_messenger.DirectMessage)

    def test_set_attributes(self):
        dir_msg = ds_messenger.DirectMessage()
        dir_msg.set_attributes('test', 'ohhimark', time.time())
        assert isinstance(dir_msg, ds_messenger.DirectMessage)
