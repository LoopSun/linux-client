#encoding=utf-8

import redis
from rq import Worker, Queue, Connection

from settings.db import REDIS_URL

# init three queue for work
listen = [
    "high",
    "default",
    "low",
]

redis_connection = redis.from_url(REDIS_URL)

if __name__ == '__main__':
    with Connection(connection=redis_connection):
        worker = Worker(map(Queue, listen))
        worker.work()
