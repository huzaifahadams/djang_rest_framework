# Generated by Django 4.1.1 on 2022-09-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='description',
            new_name='bio',
        ),
    ]
