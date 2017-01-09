#encoding=utf8

import os

# define redis connection, default is localhost and port is 6379
REDIS_URL = os.environ.get("REDIS_URL", 'redis://localhost:6379')