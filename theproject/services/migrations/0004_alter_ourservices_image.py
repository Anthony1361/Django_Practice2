# Generated by Django 4.2.4 on 2023-08-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_ourservices_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservices',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
