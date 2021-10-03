import pytest
from modules.Osm_api import OsmApi
import math

###############Check Direct Geocoding Pisitive###############    

@pytest.mark.parametrize("lat, lon, location", [('55.0282171', '82.9234509', 'Novosibirsk'), ('53.0199838', '158.6471356', 'Петропавловск-Камчатский'), ('53.0199838','158.6471356','Петропавловск-Камчатский 53'),('55.0282171','82.9234509','Novosibirsk 53')])
def test_direct_geocoding_positive(lat, lon, location):
    print('Checking direct_request')
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request()
    assert lat == lat_resp
    assert lon == lon_resp
    assert 200 == status_code


###############Check Direct Geocoding Negative###############    

@pytest.mark.parametrize("lat, lon, location", [('', '82.9234509', 'Novosibirsk 53'),('','','1'),('','82.9234509','Novosibirsk 53'),('82.9234509','82.9234509',math.pi*math.e),('55.0282171','82.9234509','asdfasfasfd')])
def test_direct_geocoding_negativ(lat, lon, location):
    lat_resp, lon_resp, status_code = OsmApi(lat, lon, location).direct_request()
    assert lat != lat_resp
    assert lon != lon_resp
    assert 200 == status_code






