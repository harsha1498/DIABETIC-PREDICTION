# Generated by Django 5.0.1 on 2024-11-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_upload_csv_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_csv_file',
            name='file',
            field=models.FileField(upload_to='csv_file/'),
        ),
    ]
