# Generated by Django 2.1.8 on 2019-06-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishdb', '0005_auto_20190610_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='line_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='fish', to='fishdb.Line'),
            preserve_default=False,
        ),
    ]
