import pytest
import requests



class FrameworkUtils:
    @staticmethod
    def API_Custom_Headers(Request_Method='Get',
                           Request_URL=None,
                           Request_json=None,
                           Request_Headers=None,
                           Expected_status_code=200,
                           ):

        request = requests.request(Request_Method,
                                   Request_URL,
                                   json=Request_json,
                                   headers=Request_Headers
                                   )
        try:
            assert request.status_code == Expected_status_code,f"Api call is fail Expected status code should bi{Expected_status_code} but getting status code {request.status_code}"
            return request

        except:
            pytest.fail(f"API call is fail we are getting{request.status_code}")
