# Generated by Django 3.2.5 on 2021-08-10 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userbase_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='user_name',
            new_name='username',
        ),
    ]
