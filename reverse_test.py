import pytest
from modules.Osm_api import OsmApi
import math

###############Check Reverse Geocoding Pisitive###############    

@pytest.mark.parametrize("lat, lon, location", [('53.047739550789935', '158.6424564500000', '53, улица Автомобилистов, 5 км, Петропавловск-Камчатский, Петропавловск-Камчатский городской округ, Камчатский край, Дальневосточный федеральный округ, 683000, Россия'),
(math.e,math.pi,'Unable to geocode')])
def test_reverse_geocoding_negativ(lat, lon, location):
    res_location, status_code = OsmApi(lat, lon, location).reverse_request()
    assert location == res_location
    assert 200 == status_code

###############Check Reverse Geocoding Negative###############

@pytest.mark.parametrize("lat, lon, location", [('53.047739550789935', '157.6424564500000', '53, улица Автомобилистов, 5 км, Петропавловск-Камчатский, Петропавловск-Камчатский городской округ, Камчатский край, Дальневосточный федеральный округ, 683000, Россия'),
(math.e,math.pi,'Piter'),('asdfsd','123131231313123', 'Piter'), ('asdafsa!!','@@@5453425','Check'), ('','','')])
def test_reverse_geocoding_negativ(lat, lon, location):
    res_location, status_code = OsmApi(lat, lon, location).reverse_request()
    assert location != res_location
    assert 200 or 400 == status_code