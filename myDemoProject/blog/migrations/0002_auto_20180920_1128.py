# Generated by Django 2.1.1 on 2018-09-20 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='Article',
        ),
    ]
