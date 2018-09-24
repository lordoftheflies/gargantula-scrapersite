# Generated by Django 2.1 on 2018-08-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='argumentmodel',
            name='tag',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='argumentmodel',
            name='data_type',
            field=models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date'), ('boolean', 'Boolean'), ('enumeration', 'Enumeration')], default='text', max_length=30),
        ),
    ]
