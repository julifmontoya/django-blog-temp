# Generated by Django 4.2.1 on 2023-06-23 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_body_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='description',
        ),
    ]
