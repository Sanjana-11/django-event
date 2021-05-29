# Generated by Django 3.2.dev20200730101900 on 2021-05-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('N-B', 'non-binary'), ('N/A', 'prefer not to say')], max_length=11, null=True),
        ),
    ]