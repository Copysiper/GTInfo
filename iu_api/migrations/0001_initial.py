# Generated by Django 3.2.3 on 2021-05-19 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackedUserObject',
            fields=[
                ('steam_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserOnlineActivityObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_playing_timestamp', models.IntegerField()),
                ('ended_playing_timestamp', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('total_played', models.FloatField()),
                ('tracked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='iu_api.trackeduserobject')),
            ],
        ),
    ]
