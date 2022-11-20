# Generated by Django 4.1.2 on 2022-11-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='document/'),
        ),
    ]
