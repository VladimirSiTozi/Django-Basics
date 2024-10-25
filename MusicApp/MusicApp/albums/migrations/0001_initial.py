# Generated by Django 5.1.2 on 2024-10-23 16:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('pm', 'Pop Music'), ('jm', 'Jazz Music'), ('rbm', '"R&B Music'), ('rm', '"Rock Music'), ('cm', 'Country Music'), ('dm', 'Dance Music'), ('hhm', 'Hip Hop Music'), ('o', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('img_url', models.ImageField(upload_to='')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='profiles.profile')),
            ],
        ),
    ]
