# Generated by Django 3.2.7 on 2021-10-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_game_win_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameteam',
            name='score',
            field=models.IntegerField(blank=True),
        ),
    ]
