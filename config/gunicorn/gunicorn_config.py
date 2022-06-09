import multiprocessing

wsgi_app = "config.asgi:application"
worker_class = "uvicorn.workers.UvicornWorker"
command = "./venv/bin/gunicorn"
pythonpath = "."
bind = ":8000"
workers = multiprocessing.cpu_count() * 2 + 1
raw_env = "DJANGO_SETTINGS_MODULE=config.settings"
errorlog = "./logs/gunicorn.log"
# max_requests = 100
