# Generated by Django 3.1.7 on 2021-03-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authormodel',
            name='face',
            field=models.ImageField(null=True, upload_to='files/authors_face/'),
        ),
    ]
