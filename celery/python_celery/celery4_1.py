from celery import Celery
from time import sleep

BROKER_URL = 'redis://localhost:6379/0'
app = Celery(main='celery1', backend='redis://localhost', broker=BROKER_URL)
# backend

@app.task
def add(x,y):
    sleep(5)
    return x+y