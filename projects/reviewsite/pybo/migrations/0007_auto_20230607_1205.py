# Generated by Django 3.1.3 on 2023-06-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20230526_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='total_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='graph',
            name='tf_idf_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review_info',
            name='review_score',
            field=models.FloatField(),
        ),
    ]
