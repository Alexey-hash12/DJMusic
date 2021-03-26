from DJMusic.celery import app
from .service import send
import logging

logger = logging.getLogger(__name__)

@app.task
def send_message(name, sender, receiver, theme, message):
	send(name, sender, receiver, theme, message)
	logger.info(f"clery sending...{name} with email: {sender} to {receiver}, theme: {theme}, message: {message}")
