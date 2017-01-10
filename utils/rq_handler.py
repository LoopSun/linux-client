#encoding=utf-8

from test.test_funs import count_words_at_url
from rq import Queue, use_connection
from utils.worker import redis_connection

def submit_work(executor, args, queue="default"):

    use_connection(redis_connection)
    q = Queue(queue)

    result = q.enqueue(executor, args)
    return result

