# Generated by Django 2.1.8 on 2019-06-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0014_auto_20190617_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='background',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fish',
            name='genotype',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fish',
            name='origin',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fish',
            name='phenotype',
            field=models.CharField(max_length=30),
        ),
    ]