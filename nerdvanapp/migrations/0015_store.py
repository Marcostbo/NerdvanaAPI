# Generated by Django 4.0.5 on 2022-09-08 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerdvanapp', '0014_add_games_via_json_pt6'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('search_name', models.CharField(max_length=60, unique=True)),
                ('link', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
    ]
