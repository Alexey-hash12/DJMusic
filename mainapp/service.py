from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

def send(name, sender, receiver, theme, message):
    send_mail(
        f"{theme}", # main text
        f"{name}, {receiver} ::: {message}", # text
        sender, # your emial
        [reciever],
        fail_silently=False
    )
    logger.info("<sending email>")
   	
