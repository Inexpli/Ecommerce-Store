# Generated by Django 3.2.5 on 2021-07-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
