# Generated by Django 2.2.2 on 2019-09-01 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
    ]