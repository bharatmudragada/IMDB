# Generated by Django 2.2.3 on 2019-07-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseQueries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]
