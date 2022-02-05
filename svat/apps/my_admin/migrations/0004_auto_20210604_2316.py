# Generated by Django 3.2.1 on 2021-06-04 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0003_auto_20210523_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=256)),
                ('status', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(default='', null=True),
        ),
    ]