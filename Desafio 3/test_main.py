from main import get_temperature
import requests
import pytest

# this class will override the current temperature to the value wich i want.
class MockResponse:
    @staticmethod
    def json():
        return {'currently' : {"temperature": 62} }

def test_get_temperature_by_lat_lng(monkeypatch):
    # calling the value.
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get) # changing the value 

    lat = -14.235004
    lng = -51.92528
    assert get_temperature(lat,lng) == 16 # Checking the value.