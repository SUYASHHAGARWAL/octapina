# Generated by Django 4.1.6 on 2023-07-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octapinapp', '0004_newuserdata_userpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuserdata',
            name='userbatch',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='username',
            field=models.CharField(max_length=120),
        ),
    ]
