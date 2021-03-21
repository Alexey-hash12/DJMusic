from DJMusic.celery import app
from .service import send
import logging

logger = logging.getLogger(__name__)

@app.task
def send_message(user_email):
	logger.info("clery sending...")
	send(user_email)