# Generated by Django 2.1.8 on 2019-06-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0007_auto_20190610_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='line_name',
            field=models.CharField(max_length=255),
        ),
    ]
