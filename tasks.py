from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def check_url(url):
    return url
