# Generated by Django 2.1 on 2018-08-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestOfferModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_city', models.CharField(max_length=25)),
                ('departure_airport', models.CharField(max_length=25)),
                ('departure_timestamp', models.DateTimeField()),
                ('arrival_airport', models.CharField(max_length=25)),
                ('arrival_date', models.DateTimeField()),
                ('region', models.CharField(max_length=25)),
                ('hotel', models.CharField(max_length=25)),
                ('stars', models.CharField(max_length=25)),
                ('room_type', models.CharField(max_length=25)),
                ('board_basis', models.CharField(max_length=25)),
                ('number_of_passangers', models.IntegerField(default=2)),
                ('duration', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
