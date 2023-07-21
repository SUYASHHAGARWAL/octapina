# Generated by Django 4.1.6 on 2023-07-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octapinapp', '0008_admin_batchinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdate', models.CharField(default='', max_length=20)),
                ('eventname', models.CharField(default='', max_length=80)),
                ('eventtime', models.CharField(default='', max_length=20)),
                ('organiser', models.CharField(default='', max_length=20)),
                ('eventlevel', models.CharField(default='', max_length=30)),
            ],
        ),
    ]