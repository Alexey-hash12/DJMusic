from django.core.mail import send_mail

def send(user_email):
    send_mail(
        "asdasd", # main text
        "dsaawds", # text
        "ryzhakovalexeynicol@gmail.com", # your emial
        [user_email],
        fail_silently=False
    )
   	
