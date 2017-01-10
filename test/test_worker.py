#encoding=utf-8

from time import sleep

from test.test_funs import count_words_at_url


if __name__ == '__main__':
    from rq import Queue, use_connection
    from utils.worker import redis_connection

    use_connection(redis_connection)
    q = Queue("low")

    result = q.enqueue(count_words_at_url, "https://www.heroku.com/")
    while not result.result:
        sleep(1)
        print(result.result)

