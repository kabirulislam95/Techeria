# Generated by Django 3.2.7 on 2021-12-01 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techeria_app', '0017_alter_myproducts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproducts',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
