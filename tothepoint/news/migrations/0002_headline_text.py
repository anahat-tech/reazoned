# Generated by Django 3.1.7 on 2021-04-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='text',
            field=models.TextField(null=True),
        ),
    ]