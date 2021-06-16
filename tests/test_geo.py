import pytest
import unittest

import requests

from requests.exceptions import ConnectionError
import responses


class TestGeo(unittest.TestCase):

    @responses.activate
    def test_simple(self):

        URL = "http://www.geoplugin.net/json.gp"
        ip = '46.139.217.99'

        responses.add(
            responses.GET, URL + '?ip=' + ip,
            status=200)

        response = requests.get(URL)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == URL + '?ip=' + ip
        assert responses.calls[0].response.text == response.text


if __name__ == '__main__':
    unittest.main()

    
    @responses.activate
    def test_exception(self):
        URL = "http://www.geoplugin.net/json.gp"
        ip = '46.139.217.99'

        responses.add(
            responses.GET, URL + '?ip=' + ip,
            body=Exception('exception'))
        with pytest.raises(Exception):
            requests.get(URL + '?ip=' + ip)

if __name__ == '__main__':
    unittest.main()


@responses.activate
def test_error():
    with pytest.raises(ConnectionError):
        requests.get('http://www.geoplugin.net/foo')

if __name__ == '__main__':
    unittest.main()
    

@responses.activate
def test_request_param():
    responses.add(
        method = responses.GET,
        url='http://www.geoplugin.net/json.gp?ip=46.139.217.99',
        body='foo',
        match_querystring=False)
    
    response = requests.get('http://www.geoplugin.net/json.gp', params={'ip' : '46.139.217.99'})
    assert responses.calls[0].request.params == {'ip' : '46.139.217.99'}

if __name__ == '__main__':
    unittest.main()
    