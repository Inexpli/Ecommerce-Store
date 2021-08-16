# Generated by Django 3.2.5 on 2021-08-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('in_stock', models.BooleanField(default=False)),
                ('promotion', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]
