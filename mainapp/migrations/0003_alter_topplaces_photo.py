# Generated by Django 3.2.19 on 2024-02-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_topplaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topplaces',
            name='photo',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]