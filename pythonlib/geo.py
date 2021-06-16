import requests
from requests.auth import HTTPDigestAuth
import json

import logging
logging.basicConfig(filename='geo.log', encoding='utf-8', level=logging.DEBUG)

class Geo():

    def getResponse(self):

        URL = 'http://www.geoplugin.net/json.gp'
        ip = '46.139.217.99'
        PARAMS = {'ip': ip}

        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        data1 = json.dumps(data)
        data2 = json.loads(data1)

        result = dict()

        try:

            for key, value in data2.items(): 
                if key == 'geoplugin_city':
                    result[key] = value
                if key == 'geoplugin_countryName':
                    result[key] = value
                if key == 'geoplugin_region':
                    result[key] = value
                if key == 'geoplugin_timezone':
                    result[key] = value
                if key == 'geoplugin_latitude':
                    result[key] = value
                if key == 'geoplugin_longitude':
                    result[key] = value

            print(result)
            logging.info('Successfully GET method at http://www.geoplugin.net/json.gp?ip=46.139.217.99')

        except requests.exceptions.Timeout:
            logging.error('Request time out at http://www.geoplugin.net/json.gp?ip=46.139.217.99')
        except requests.exceptions.TooManyRedirects:
            logging.error('Too many redirects at http://www.geoplugin.net/json.gp?ip=46.139.217.99')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

geo = Geo()
print(geo.getResponse())
