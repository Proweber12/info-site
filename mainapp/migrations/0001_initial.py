# Generated by Django 4.0.3 on 2022-03-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512)),
                ('location', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=512)),
                ('question', models.TextField()),
                ('agree_privacy', models.BooleanField()),
            ],
        ),
    ]
