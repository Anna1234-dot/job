# Generated by Django 4.0.4 on 2022-07-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_company_address_job_company_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_size',
            field=models.CharField(choices=[('size_1-9', '1-9'), ('size_10-49', '10-49'), ('size_50-99', '50-99'), ('size_100', '100+')], default='size_1-9', max_length=20),
        ),
    ]
