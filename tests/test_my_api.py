import unittest

import requests

from requests.exceptions import ConnectionError
import responses

class TestMyApi(unittest.TestCase):

    @responses.activate
    def test_my_api(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'http://www.geoplugin.net/json.gp?ip=46.139.217.99',
                 body='{}', status=200,
                 content_type='application/json')
        resp = requests.get('http://www.geoplugin.net/json.gp?ip=46.139.217.99')

        assert resp.status_code == 200

if __name__ == '__main__':
    unittest.main()
