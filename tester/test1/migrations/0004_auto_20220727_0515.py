# Generated by Django 3.1.12 on 2022-07-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_auto_20220727_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
