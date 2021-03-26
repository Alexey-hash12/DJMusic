## Party: Леха Р, Сергей Ч, Саня Р, Саня З.
Start of development: 20 march 2021
End of development: ...

## toolkit
-Django
-Django Rest Framework
-Django Celery
-Django Redis(Cache)
-Logging
-Postgresql
-SMTP
-Captcha
-Websockets
## Tasks: tasks.pdf

**Language**: En language
**Comments**: En language

# Start of project
***at first you should install requirements***
```bash
pip install -r requirements.txt
```
***and migrate***
```bash
python manage.py migrate
```
***next you should runserver***
```bash
python manage.py makemigration
```

## Site
[mysite]:...



# Documentation
This site is designed for quick access to listening to the music of famous artists. The user has 3 statuses: SILVER, GOLD, PLATINUM. Silver's status is free. On the Silver status, you can listen to the music of different artists, except for the music of the gold status. This music can be listened to by a user with the Gold status. Silver can also create playlists with the music selected by the user, and there is also a section: liked music. Users can subscribe to the artist. PLATINUM status - the status of the performer, i.e. the user can either subscribe and listen to music, or add their own. The site has a system for selecting tracks recommended for listening, sending them by e-mail, registering via social networks (also qr code), as well as a chat for subscribers.



# DEVELOPMENT
## First Part:

**Сергей Ч**: 
Django auth + profile + celery(email)


**Саня З**:
websockets + celery

**Саня Р**:
mainapp(patterns + form_validation(captcha)) + django_redis cache

**Леха R**:
RestApi + DeppLearning

## Second Part:
....


#Nessesary information
##email
denied info: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PPTD34ZDNRL8gcB81SWMgilQFRhfjdKwlCy2A0vYBWguVlXHpAZja-Y7RpiECOYpXpiDVlnuoLm2QkGo30vNFO3zWSdg

##celery
```bash
	celery -A {name of celery application} worker
```

##docker
docker install: install docker desctop

****
docker instal additional software:https://docs.microsoft.com/ru-ru/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

****
entrypoin.sh -> unix(LF)

****
docker-amd64-error:https://stackoverflow.com/questions/48066994/docker-no-matching-manifest-for-windows-amd64-in-the-manifest-list-entries

****
docker-run: https://stackoverflow.com/questions/52946810/error-during-connect-get-http-2f2f-2fpipe2fdocker-engine-v1-38-info

