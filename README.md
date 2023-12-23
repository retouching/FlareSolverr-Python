<div align="center">
    <h1>FlareSolverr - Python API</h1>
    Simple python API to use a <a href="https://github.com/FlareSolverr/FlareSolverr">FlareSolverr</a> Service
</div>

## Requirements:

- A <a href="https://github.com/FlareSolverr/FlareSolverr">FlareSolverr</a> instance
- requests
- beautifulsoup4 (to parse HTML pages)

## Usage:

### Normal:

```python
from flaresolverr import FlareSolverr

# Get page protected by Cloudflare
FlareSolverr.get(
    'https://crunchyroll.com/rss',
    flaresolverr_base_url='http://flaresolverr:5000'  # if url is different from base
)  # -> return a "Response" instance
```

All parameters can be found in "FlareSolverr" class

### Using session:

```python
from flaresolverr.session import FlareSolverrSession

# Create session
session = FlareSolverrSession.create(
    proxy='http://dummy',  # You can pass a proxy to use with credentials here if any
    flaresolverr_base_url='http://flaresolverr:5000'  # if url is different from base
)

# Get page protected by Cloudflare
session.get(
    'https://crunchyroll.com/rss',
)  # -> return a "Response" instance

# Session must be closed at end
session.destroy()

# You can also list sessions already created
FlareSolverrSession.get_sessions()  # return list of sessions id created and not closed
```