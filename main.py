from celery import Celery
from fastapi import FastAPI
from project import create_app, create_celery

app = create_app()
celery = create_celery()


@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y