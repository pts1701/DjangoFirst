# Generated by Django 4.1.3 on 2022-11-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='info',
            field=models.CharField(default='description', max_length=150),
        ),
    ]