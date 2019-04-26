# Generated by Django 2.2 on 2019-04-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zebrafish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=20)),
                ('line_number', models.CharField(max_length=20)),
                ('line_type', models.CharField(choices=[('wt', 'WT'), ('tg', 'Tg'), ('mu', 'Mutant'), ('cko', 'CRISPR KO'), ('cki', 'CRISPR KI'), ('other', 'Other')], max_length=5)),
                ('background', models.CharField(max_length=20)),
                ('genotype', models.CharField(max_length=20)),
                ('phenotype', models.CharField(max_length=20)),
                ('origin', models.CharField(max_length=20)),
                ('availability', models.CharField(choices=[('live', 'Live'), ('cryo', 'Cryopreserved'), ('both', 'Live & Cryopreserved')], max_length=4)),
                ('comments', models.TextField()),
                ('link', models.URLField()),
                ('mta', models.BooleanField(default=False, verbose_name='MTA')),
            ],
        ),
    ]
