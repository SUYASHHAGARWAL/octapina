# Generated by Django 4.2.4 on 2023-08-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenum', models.CharField(default='', max_length=12)),
                ('adminname', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='BatchInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(default='', max_length=100)),
                ('Batchfees', models.CharField(default='', max_length=12)),
                ('BatchDfees', models.CharField(default='', max_length=12)),
                ('duration', models.CharField(default='', max_length=12)),
                ('startdate', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=14)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
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
        migrations.CreateModel(
            name='NewUserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=120)),
                ('useremail', models.CharField(default='', max_length=120)),
                ('usermobile', models.CharField(default='', max_length=120)),
                ('usercity', models.CharField(default='', max_length=120)),
                ('userdob', models.CharField(default='', max_length=120)),
                ('usergender', models.CharField(default='', max_length=120)),
                ('guardiansname', models.CharField(default='', max_length=120)),
                ('guardiansphone', models.CharField(default='', max_length=120)),
                ('userschool', models.CharField(default='', max_length=120)),
                ('userclass', models.CharField(default='', max_length=120)),
                ('userpassword', models.CharField(default='', max_length=30)),
                ('userbatch', models.CharField(default='', max_length=200)),
                ('batch_purchased', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
