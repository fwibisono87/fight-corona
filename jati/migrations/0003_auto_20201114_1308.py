# Generated by Django 3.0.9 on 2020-11-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jati', '0002_auto_20201114_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengalaman',
            name='cerita_pengalaman',
            field=models.CharField(max_length=1000),
        ),
    ]
