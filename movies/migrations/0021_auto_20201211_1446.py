# Generated by Django 3.1.2 on 2020-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_auto_20201211_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magnet',
            name='link',
            field=models.CharField(max_length=2083),
        ),
    ]