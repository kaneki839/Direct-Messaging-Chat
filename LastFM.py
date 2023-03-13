"""
LastFM class
"""
# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

from WebAPI import WebAPI


class LastFm(WebAPI):
    """
    LastFm class that contain music related information
    """
    def __init__(self, artist: str, album: str) -> None:
        self.artist = artist
        self.album = album

        self.alltracks = None

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.
        '''
        url = f"http://ws.audioscrobbler.com//2.0/?method=album.getinfo&" \
            f"api_key={LastFm.apikey}&artist={self.artist}&" \
            f"album={self.album}&format=json"
        self._download_url(url)
        tracks = LastFm.response['album']['tracks']['track']
        all_track = [info['name'] for info in tracks if 'name' in info]
        self.alltracks = all_track

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        if '@lastfm' in message:
            message = message.replace('@lastfm', self.artist)
        return message
