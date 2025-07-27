from celery import Celery
from app.core.email import send_email
from app.core.config import settings

celery = Celery("notification", broker=settings.REDIS_BROKER_URL)

@celery.task
def send_registration_email(to: str):
    send_email(
        to=to,
        subject="Welcome!",
        body="Thanks for registering. We're glad to have you!"
    )

@celery.task
def send_order_email(to: str, order_total: float):
    send_email(
        to=to,
        subject="Order Confirmation",
        body=f"Thank you for your order!\nTotal: ₹{order_total}"
    )
