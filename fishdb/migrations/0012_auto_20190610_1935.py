# Generated by Django 2.1.8 on 2019-06-10 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0011_auto_20190610_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='fish',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='fish', to='fishdb.Location'),
            preserve_default=False,
        ),
    ]
