# Generated by Django 5.0.1 on 2024-11-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_upload_csv_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_csv_file',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]