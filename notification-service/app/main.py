from fastapi import FastAPI
from app.workers.tasks import send_registration_email

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Notification service running"}

@app.post("/test-email")
def test_email():
    send_registration_email.delay("test@example.com")
    return {"msg": "Email queued"}
