# Generated by Django 3.2.5 on 2021-08-05 15:06

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210727_0117'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('products', django.db.models.manager.Manager()),
            ],
        ),
    ]
