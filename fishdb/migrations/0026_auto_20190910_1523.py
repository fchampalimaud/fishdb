# Generated by Django 2.1.8 on 2019-09-10 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0025_auto_20190812_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fishdb_fish_related', to='fishdb.Category'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fishdb_fish_related', to='fishdb.Species'),
        ),
    ]