# Generated by Django 2.1.8 on 2019-07-10 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0021_auto_20190710_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='location',
        ),
    ]