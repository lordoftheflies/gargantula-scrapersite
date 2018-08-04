# Generated by Django 2.0.7 on 2018-07-09 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mdm', '0001_initial'),
        ('datastore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestOfferJobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrapy_job', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('state', models.CharField(blank=True, choices=[('pending', 'Pending'), ('finished', 'Finished'), ('running', 'Running')], default=None, max_length=30, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ComparisonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PortalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('version', models.CharField(default='3.13.54', max_length=10)),
                ('lua_source', models.FileField(blank=True, default=None, null=True, upload_to='source')),
                ('scrapy', models.CharField(choices=[('appcrawler', 'SPA Crawler'), ('portalcrawler', 'Web Crawler'), ('nomono', 'Nomono Crawler'), ('bot', 'Web bot')], default='portalcrawler', max_length=250)),
                ('spider', models.CharField(choices=[('angular', 'Angular'), ('screenshot', 'Screenshot'), ('json', 'Json'), ('xml', 'Xml')], default='portalcrawler', max_length=200)),
                ('supplier', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mdm.SupplierModel')),
            ],
            options={
                'verbose_name': 'portal',
                'verbose_name_plural': 'portals',
            },
        ),
        migrations.AddField(
            model_name='comparisonmodel',
            name='competitors',
            field=models.ManyToManyField(related_name='compared_portals', to='botapp.PortalModel'),
        ),
        migrations.AddField(
            model_name='comparisonmodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_portals', to='botapp.PortalModel'),
        ),
        migrations.AddField(
            model_name='bestofferjobmodel',
            name='comparison',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='botapp.ComparisonModel'),
        ),
        migrations.AddField(
            model_name='bestofferjobmodel',
            name='data',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='datastore.BestOfferModel'),
        ),
        migrations.AddField(
            model_name='bestofferjobmodel',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='botapp.BestOfferJobModel'),
        ),
        migrations.AddField(
            model_name='bestofferjobmodel',
            name='portal',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='botapp.PortalModel'),
        ),
    ]
