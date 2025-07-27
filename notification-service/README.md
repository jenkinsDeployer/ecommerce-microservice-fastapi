notification-service/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── email.py
│   ├── workers/
│   │   └── tasks.py
│   └── main.py
├── celery_worker.py
├── .env
├── requirements.txt
└── README.md

start redis server:
- redis-server

start celery worker:
- celery -A app.workers.tasks worker --loglevel=info


uvicorn app.main:app --reload --port 8003
