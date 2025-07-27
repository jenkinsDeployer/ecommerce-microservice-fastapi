cart-order-service/
├── app/
│   ├── api/
│   │   └── routes_cart_order.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── cart.py
│   │   └── order.py
│   ├── schemas/
│   │   ├── cart.py
│   │   └── order.py
│   ├── services/
│   │   └── cart_order.py
│   └── main.py
├── .env
└── README.md

uvicorn app.main:app --reload --port 8002
