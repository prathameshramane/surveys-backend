# Generated by Django 4.1.1 on 2022-09-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ('time',)},
        ),
    ]
