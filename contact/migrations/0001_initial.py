# Generated by Django 4.0.4 on 2022-08-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=20)),
                ('ContactNumber', models.CharField(max_length=20)),
                ('Mails', models.CharField(max_length=60)),
                ('Messages', models.TextField()),
            ],
        ),
    ]
