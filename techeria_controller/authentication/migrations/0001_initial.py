# Generated by Django 3.2.7 on 2021-11-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'buyer',
            },
        ),
        migrations.CreateModel(
            name='SellerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]