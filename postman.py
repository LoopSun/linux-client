# encoding=utf-8

"""
This is a daemon to post data(exclude instructions).


main logic:

  1. daemon monitor message queue
  2. if queue has message, daemon send the message to

data format:

{
    "uuid": "d2cd6fee-dbf5-11e6-8e80-0090f5f166e1",
    "type": 1,      # 1: node_monitor_message
                    # 2: web_monitor_message
                    # 3: remote_command_message
                    # 4: remote_script_message
                    # 5: process_manager_message
                    ## 6: more message type(wait for define)
    "context": {    # changeable context payload
        "name": "dnsmasq",  # message name, to identify the message owner
        "message": "restart success",  # operation message
        "time": "2017-1-16 22:38:02",  # operation complete time
    }
    "post_time": "2017-1-16 22:39:30"
}

"""

import requests

from settings.server import POST_SERVER
#todo: to complete data crypto logic
from utils import data_crypto

#todo: To complete queue logic
DATA_QUEUE = ""

@data_crypto
def post_data(data):
    """

    send the data to remote server.

    :param data: post data
    :return: delete posted message
    """
    try:
        response = requests.post(POST_SERVER, data=data)
        if response == 200:
            return delete_message
        else:
            pass
    except ConnectionError as err:
        pass
    except Exception as err:
        pass


def post_control():
    pass


def get_message():
    pass


def delete_message():
    pass

