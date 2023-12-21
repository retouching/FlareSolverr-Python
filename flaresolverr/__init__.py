import requests

from flaresolverr.response import Response


class FlareSolverr:
    @staticmethod
    def _request(url, max_timeout=60_000, cookies=None, proxy=None, post_data=None, flaresolverr_base_url=None):
        base_url = flaresolverr_base_url or 'http://localhost:8191'
        if base_url.endswith('/'):
            base_url = base_url[:-1]

        if post_data is not None:
            request_type = 'request.post'
            encoded = ''

            if not isinstance(post_data, dict):
                raise ValueError('Post data must be a dict')

            for key in post_data:
                encoded += f'{str(key)}={str(post_data[key])}&'

            post_data = encoded[:-1]
        else:
            request_type = 'request.get'

        if not isinstance(max_timeout, int):
            max_timeout = int(max_timeout)

        res = requests.post(f'{base_url}/v1', json={
            'cmd': request_type,
            'url': url,
            'maxTimeout': max_timeout,
            'cookies': cookies,
            'proxy': proxy,
            'postData': post_data
        })

        return Response(res, base_url)

    @staticmethod
    def get(url, max_timeout=60_000, cookies=None, proxy=None, flaresolverr_base_url=None):
        return FlareSolverr._request(url, max_timeout, cookies, proxy, flaresolverr_base_url)

    @staticmethod
    def post(url, max_timeout=60_000, cookies=None, proxy=None, post_data=None, flaresolverr_base_url=None):
        return FlareSolverr._request(url, max_timeout, cookies, proxy, post_data, flaresolverr_base_url)
