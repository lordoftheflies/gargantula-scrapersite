# Generated by Django 2.0.7 on 2018-07-09 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('report_builder', '0006_auto_20180413_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='report_builder.Report')),
            ],
        ),
    ]
