# Generated by Django 4.0.3 on 2022-05-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(default='', max_length=50)),
                ('Cnic', models.CharField(default='', max_length=50)),
                ('DOB', models.CharField(default=0, max_length=50)),
                ('Adress', models.CharField(max_length=300)),
            ],
        ),
    ]
