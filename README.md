# Celery + FastAPI + Redis + Flower

https://testdriven.io/courses/fastapi-celery/getting-started/

```bash
uvicorn main:app --reload --port 8000
celery -A main.celery worker --loglevel=info
celery -A main.celery flower --port=5555
```
