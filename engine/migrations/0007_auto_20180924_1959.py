# Generated by Django 2.1 on 2018-09-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_auto_20180920_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmodel',
            name='notebook',
            field=models.FilePathField(max_length=500, path='/home/lordoftheflies/Documents/theoutsourcepro/gargantula-scrapersite/../notebooks'),
        ),
    ]
