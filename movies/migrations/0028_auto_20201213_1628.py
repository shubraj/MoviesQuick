# Generated by Django 3.1.2 on 2020-12-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0027_auto_20201212_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbID',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]