"""
testing module that test the ds_messenger module
"""
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
                                                  'mikey', '0123')
        assert sender_obj.send('testing again', 'ohhimark') is True
        for obj in sender_obj.retrieve_new():
            assert isinstance(obj, ds_messenger.DirectMessage)
        for obj in sender_obj.retrieve_all():
            assert isinstance(obj, ds_messenger.DirectMessage)


if __name__ == "__main__":
    unittest.main()
