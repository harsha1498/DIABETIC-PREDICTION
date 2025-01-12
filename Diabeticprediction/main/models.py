from django.db import models
from django.core.exceptions import ValidationError
import os

# Custom validator to allow only CSV files
def validate_csv_file(value):
    if not value.name.endswith('.csv'):
        raise ValidationError("Only CSV files are allowed.")

class Upload_csv_file(models.Model):
    file = models.FileField(upload_to="csv_file/", validators=[validate_csv_file])  # Use the custom validator
    upload_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure only one file is allowed in the database by deleting the previous record
        if not self.pk:
            # Ensure there's only one record in the database
            if Upload_csv_file.objects.exists():
                # If a file already exists, delete it before saving the new one
                existing_file = Upload_csv_file.objects.first()
                if existing_file and existing_file.file:
                    if os.path.exists(existing_file.file.path):
                        os.remove(existing_file.file.path)  # Delete the old file
                    existing_file.delete()  # Delete the old record
        self.name = self.file.name  # Set the name field to the uploaded file's name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "No Name"
