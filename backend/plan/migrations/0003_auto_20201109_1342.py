# Generated by Django 3.1.3 on 2020-11-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20201109_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='gallery_thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
