# Generated by Django 3.0.3 on 2020-04-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seds_blogs', '0009_vlog_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Astrophotography_trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Astrophotography_link', models.CharField(max_length=400)),
            ],
        ),
    ]
