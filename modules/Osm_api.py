import requests
from modules.Parser_xml import XmlParser

class OsmApi:


    def __init__(self, lat: int, lon: int, location: str, format : str ='xml', zoom: int = 18):
        """
                Входные параметры:
                lan - значение широты
                lon - значение долготы
                location - имя локации
                format - формат запроса в сторону OSM (def = xml)
                zoom - маштабируемость
        """
        self.lat_value = lat
        self.url = None
        self.lon_value = lon
        self.location = location
        self.format = format
        self.zoom = zoom

    def get_request(self):
        """
                Получение ответа с сервера Osm
        """
        return requests.get(self.url)

    
    def direct_request(self):
        """
                Проверка прямого геокодирования, передача имени локации
        """
        self.url = f'https://nominatim.openstreetmap.org/search?q={self.location}&format={self.format}'
        response = self.get_request()
        if len(XmlParser().direct_parser(response.content)) == 0:
            lat, lon = [None, None]
        else:
            lat, lon = self.result_analysis(XmlParser().direct_parser(response.content))
        return lat, lon, response.status_code

    def reverse_request(self):
        """
                Проверка обратного геокодирования, передача долготы и широты
        """
        self.url = f'https://nominatim.openstreetmap.org/reverse.php?lat={self.lat_value}&lon={self.lon_value}&zoom={self.zoom}&format={self.format}'
        response = self.get_request()
        location = XmlParser().reverse_parser(response.content)
        return location, response.status_code


    def result_analysis(self, search_results: list):
        """
                Сравнивает полученные значения широты и долготы с заданными в тесте.
        """
        for num, ind in enumerate(search_results, 1):
            lat = ind.get("lat")
            lon = ind.get("lon")
            if str(self.lat_value) == lat and str(self.lon_value) == lon:
                return  lat, lon
            elif len(search_results) == num:
                return lat, lon
            