# Generated by Django 3.1.3 on 2023-05-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20230522_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='poster_src',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
