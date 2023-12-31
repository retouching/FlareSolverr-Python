from bs4 import BeautifulSoup

from flaresolverr.excpetion import FlareSloverrException


class Response:
    def __init__(self, request_response, request_url, flaresloverr_url):
        self._request_response = request_response
        self._request_url = request_url
        self._flaresloverr_url = flaresloverr_url

        self._data = request_response.json()

    @property
    def flaresloverr(self):
        return {
            'url': self._flaresloverr_url,
            'version': self._data.get('version')
        }

    @property
    def raw(self):
        return self._data.get('solution').get('response')

    @property
    def html(self):
        return BeautifulSoup(self._data.get('solution').get('response'), 'html.parser')

    @property
    def start_timestamp(self):
        return self._data.get('startTimestamp')

    @property
    def end_timestamp(self):
        return self._data.get('endTimestamp')

    @property
    def is_ok(self):
        return self._data.get('status') == 'ok'

    @property
    def cookies(self):
        return self._data.get('solution', {}).get('cookies') or {}

    @property
    def status_code(self):
        return self._data.get('solution', {}).get('status')

    @property
    def url(self):
        return self._data.get('solution', {}).get('url') or self._request_url

    @property
    def message(self):
        return self._data.get('message')

    def raise_for_status(self):
        if not self.is_ok:
            raise FlareSloverrException(self.message or 'Unknown error occured', self)

        if self.status_code is None or self.status_code > 299:
            raise FlareSloverrException(
                f'Page return HTTP {self.status_code} error' if self.status_code else 'Unknown error occured', self)

    @property
    def headers(self):
        return {
            **self._data.get('solution').get('headers'),
            'User-Agent': self._data.get('solution', {}).get('userAgent')
        }
