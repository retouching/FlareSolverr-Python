import requests

from flaresolverr import FlareSolverr


class FlareSolverrSession:
    def __init__(self, session_id, flaresolverr_base_url=None):
        self.session_id = session_id

        self.base_url = flaresolverr_base_url or 'http://localhost:8191'
        if self.base_url.endswith('/'):
            self.base_url = self.base_url[:-1]

    @staticmethod
    def create(session_id=None, proxy=None, flaresolverr_base_url=None):
        base_url = flaresolverr_base_url or 'http://localhost:8191'
        if base_url.endswith('/'):
            base_url = base_url[:-1]

        res = requests.post(f'{base_url}/v1', json={
            'cmd': 'sessions.create',
            'session': session_id,
            'proxy': proxy
        })
        res.raise_for_status()

        return FlareSolverrSession(
            res.json().get('session'),
            flaresolverr_base_url
        )

    @staticmethod
    def get_sessions(flaresolverr_base_url=None):
        base_url = flaresolverr_base_url or 'http://localhost:8191'
        if base_url.endswith('/'):
            base_url = base_url[:-1]

        res = requests.post(f'{base_url}/v1', json={
            'cmd': 'sessions.list'
        })
        res.raise_for_status()

        return res.json()

    def destroy(self):
        res = requests.post(f'{self.base_url}/v1', json={
            'cmd': 'sessions.destroy',
            'session': self.session_id
        })
        res.raise_for_status()

    def get(self, url, max_timeout=60_000, cookies=None):
        return FlareSolverr.get(url, max_timeout, cookies, None, self.session_id, self.base_url)

    def post(self, url, max_timeout=60_000, cookies=None, post_data=None):
        return FlareSolverr.post(url, max_timeout, cookies, None, post_data, self.session_id, self.base_url)
