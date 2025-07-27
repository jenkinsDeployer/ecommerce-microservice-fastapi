auth-service/
├── app/
│   ├── api/               # Routes
│   │   └── routes_auth.py
│   ├── core/              # Config, JWT
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── services/
│   │   └── auth.py
│   └── main.py
├── requirements.txt
└── .env


uvicorn app.main:app --reload
uvicorn app.main:app --reload --port 8005