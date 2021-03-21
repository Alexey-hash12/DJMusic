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
pip install -r req.txt
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


