# Generated by Django 3.1.7 on 2021-04-03 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_headline_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Headline',
            new_name='Headlines',
        ),
    ]