# Generated by Django 3.2.7 on 2021-10-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
