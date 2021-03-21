# Generated by Django 3.1.2 on 2021-03-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_authormodel_face'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('poster', models.ImageField(upload_to='files/Albums_poster')),
                ('date', models.DateTimeField()),
                ('music', models.ManyToManyField(to='mainapp.MusicModel')),
            ],
        ),
        migrations.AddField(
            model_name='authormodel',
            name='albums',
            field=models.ManyToManyField(to='mainapp.Albums'),
        ),
    ]