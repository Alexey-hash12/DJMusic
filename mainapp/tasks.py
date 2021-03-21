from DJMusic.celery import app
from .service import send

@app.task
def send_message(user_email):
	print('yes')
	send(user_email)