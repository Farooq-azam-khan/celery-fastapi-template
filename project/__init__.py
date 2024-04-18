from fastapi import FastAPI
from celery import Celery




def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app


def create_celery():
    return Celery(
        __name__,
        broker="redis://127.0.0.1:6379/0",
        backend="redis://127.0.0.1:6379/0"
    )