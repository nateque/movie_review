# Generated by Django 2.0 on 2020-03-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=5000),
        ),
    ]
