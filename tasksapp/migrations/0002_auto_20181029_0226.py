# Generated by Django 2.2 on 2018-10-29 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TasksDB',
            new_name='Task',
        ),
    ]
