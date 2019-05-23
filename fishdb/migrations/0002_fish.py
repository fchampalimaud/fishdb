# Generated by Django 2.1.8 on 2019-05-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('background', models.CharField(max_length=20)),
                ('genotype', models.CharField(max_length=20)),
                ('phenotype', models.CharField(max_length=20)),
                ('origin', models.CharField(max_length=20)),
                ('availability', models.CharField(choices=[('live', 'Live'), ('cryo', 'Cryopreserved'), ('both', 'Live & Cryopreserved'), ('none', 'Unavailable')], max_length=4)),
                ('comments', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('mta', models.BooleanField(default=False, verbose_name='MTA')),
                ('line_name', models.CharField(max_length=20)),
                ('line_number', models.CharField(max_length=20)),
                ('line_type', models.CharField(choices=[('wt', 'WT'), ('tg', 'Tg'), ('mu', 'Mutant'), ('cko', 'CRISPR KO'), ('cki', 'CRISPR KI'), ('other', 'Other')], max_length=5)),
                ('line_type_other', models.CharField(blank=True, max_length=20, verbose_name='')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('species', models.ForeignKey(db_column='species', on_delete=django.db.models.deletion.PROTECT, to='fishdb.Species')),
            ],
            options={
                'verbose_name': 'fish',
                'verbose_name_plural': 'fish',
                'abstract': False,
            },
        ),
    ]
