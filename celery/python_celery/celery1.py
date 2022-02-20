# pip install celery

from celery import Celery
from time import sleep

BROKER_URL = 'redis://localhost:6379/0'
app = Celery(main='celery1', broker=BROKER_URL)
# main --> module name

@app.task
def add(x,y):
    sleep(15)
    return x+y


# run by :
# celery -A celery1 worker --loglevel=info

# import :
# https://riptutorial.com/celery/example/23628/celery-plus-redis