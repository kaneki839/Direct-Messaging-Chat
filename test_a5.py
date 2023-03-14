"""
testing whole program
"""

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import unittest
from OpenWeather import OpenWeather
from LastFM import LastFm


class TestTwoClass(unittest.TestCase):
    """
    testing OpenWeather and LastFM
    """
    def test_open_weather(self):
        """
        testing openweather
        """
        zipcode = '92697'
        ccode = 'US'
        apikey = "bb34f51838f49bca2be3d07c1285afa1"
        open_weather = OpenWeather(zipcode, ccode)
        open_weather.set_apikey(apikey)
        assert open_weather.apikey is not None
        open_weather.load_data()
        assert open_weather.city == 'Irvine'
        assert open_weather.temperature is not None
        assert open_weather.high_temperature is not None
        assert open_weather.low_temperature is not None
        assert open_weather.longitude is not None
        assert open_weather.latitude is not None
        assert open_weather.description is not None
        assert open_weather.humidity is not None
        assert open_weather.city is not None
        assert open_weather.sunset is not None
        assert open_weather.transclude('@weather') == open_weather.description

    def test_lastfm(self):
        """
        testing lastfm
        """
        artist = 'keshi'
        album = 'GABRIEL'
        apikey = "805379ee63e55d5dba6a123ab70e48f5"
        lastfm = LastFm(artist, album)
        lastfm.set_apikey(apikey)
        assert lastfm.apikey is not None
        lastfm.load_data()
        assert lastfm.alltracks == ['GET IT', 'SOMEBODY', 'WESTSIDE', 'touch',
                                    'MILLI', 'PÉRE', 'HELL/HEAVEN',
                                    'ANGOSTURA', 'understand', 'LIMBO',
                                    'ANGEL', 'GABRIEL']
        assert lastfm.transclude('@lastfm') == lastfm.artist


if __name__ == "__main__":
    unittest.main()
