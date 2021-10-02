# Generated by Django 3.2.7 on 2021-10-01 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_player_height'),
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='win_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_games', to='teams.team'),
        ),
    ]
