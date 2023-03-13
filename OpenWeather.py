"""
OpenWeather Class
"""
# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

from WebAPI import WebAPI


class OpenWeather(WebAPI):
    """
    OpenWeather class that contain weather information
    """

    def __init__(self, zipcode: str, ccode: str) -> None:
        self.zipcode = zipcode
        self.ccode = ccode

        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.
        '''
        url = f"http://api.openweathermap.org/data/2.5/weather?" \
            f"zip={self.zipcode},{self.ccode}&appid={OpenWeather.apikey}"
        self._download_url(url)

        self.temperature = self.response['main']['temp']
        self.high_temperature = self.response['main']['temp_max']
        self.low_temperature = self.response['main']['temp_min']
        self.longitude = self.response['coord']['lon']
        self.latitude = self.response['coord']['lat']
        self.description = self.response['weather'][0]['description']
        self.humidity = self.response['main']['humidity']
        self.city = self.response['name']
        self.sunset = self.response['sys']['sunset']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        if '@weather' in message:
            message = message.replace('@weather', self.description)
        return message
