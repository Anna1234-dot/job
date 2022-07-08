# Generated by Django 4.0.4 on 2022-07-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Активно'), ('employed', 'Занято'), ('archived', 'Архивировано')], default='active', max_length=20),
        ),
    ]
