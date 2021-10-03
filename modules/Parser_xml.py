from xml.etree import ElementTree

class XmlParser():

    """
       Парсер xml значений от response (при прямом и обратном геокодировании)    
    """

    def direct_parser(self, response: bytes):
        search_results = []
        body_string = ElementTree.ElementTree(response.decode()).getroot()
        body_xml = ElementTree.fromstring(body_string)
        for child in body_xml:
            search_results.append(
                {
                    "lat": child.attrib.get('lat'),
                    "lon": child.attrib.get('lon')
                }
            )
        return search_results

    def reverse_parser(self, response: bytes):
        body_string = ElementTree.ElementTree(response.decode()).getroot()
        body_xml = ElementTree.fromstring(body_string)
        location = body_xml[0].text
        return location