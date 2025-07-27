product-service/
├── app/
│   ├── api/
│   │   └── routes_product.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── product.py
│   ├── schemas/
│   │   └── product.py
│   ├── services/
│   │   └── product.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md

uvicorn app.main:app --reload --port 8001
