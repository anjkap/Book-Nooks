# Generated by Django 4.2.5 on 2023-10-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_alter_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100),
        ),
    ]
