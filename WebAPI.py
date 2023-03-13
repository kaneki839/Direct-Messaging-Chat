"""
Base API class that can be inherited by other class
"""
# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

from abc import ABC, abstractmethod
import sys
import json
from urllib import request, error


class _503Error(Exception):
    pass


class _404Error(Exception):
    pass


class WebAPI(ABC):
    """
    Base API class that contains method can be used by other child class
    """
    apikey = None
    response = None

    def _download_url(self, url: str) -> dict:
        request_resp = None
        try:
            request_resp = request.urlopen(url)
            json_results = request_resp.read()
            WebAPI.response = json.loads(json_results)
        except error.HTTPError as err:
            print('Failed to download contents of URL')
            print(f'Status code: {err.code}')
            if err.code == 404:
                raise _404Error(f'{err.code} (Page Not Found)') from err
            if err.code == 503:
                raise _503Error(f'{err.code} (Service Unavailable)') from err
        except error.URLError as err:
            sys.exit(f'Invalid API url: {err} \nOR\nLoss connection to' +
                     ' the internet')
        except json.JSONDecodeError:
            sys.exit('Invalid data formatting from the remote API')
        finally:
            if request_resp is not None:
                request_resp.close()

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        WebAPI.apikey = apikey

    @abstractmethod
    def load_data(self):
        '''
        Load the data from api call
        '''

    @abstractmethod
    def transclude(self, message: str) -> str:
        '''
        tranclude keyword contained in message to the data from api
        '''
