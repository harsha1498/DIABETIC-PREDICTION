# Generated by Django 5.0.1 on 2024-11-23 09:10

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_upload_csv_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_csv_file',
            name='file',
            field=models.FileField(upload_to='csv_file/', validators=[main.models.validate_csv_file]),
        ),
    ]
