#encoding=utf8

import os

# define the server address the agent should to notice

POST_SERVER = os.environ.get("POST_SERVER")

# post interval, to avoid DDOS server

POST_INTERVAL = os.environ.get("POST_INTERVAL", 3)
