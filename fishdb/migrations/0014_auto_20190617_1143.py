# Generated by Django 2.1.8 on 2019-06-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0013_fish_line_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='line_number',
            field=models.PositiveIntegerField(),
        ),
    ]