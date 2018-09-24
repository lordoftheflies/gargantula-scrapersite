# Generated by Django 2.1 on 2018-09-19 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20180829_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=1000)),
                ('cause', models.CharField(blank=True, default=None, max_length=1000, null=True)),
            ],
        ),
    ]
