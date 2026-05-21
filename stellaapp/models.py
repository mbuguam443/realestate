from django.db import models

# Create your models here.
# models.py
from django.db import models


class Property(models.Model):
    # Property title e.g. "Lodgeville Road"
    title = models.CharField(max_length=200)

    # Short description of the property
    description = models.TextField()

    # Property location e.g. "High Meadow Lane Mount Pleasant"
    location = models.CharField(max_length=255)

    # Property price e.g. 170000
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # Property size e.g. 900 sq ft
    area = models.PositiveIntegerField(help_text="Area in square feet")

    # Number of bedrooms e.g. 4
    bedrooms = models.PositiveIntegerField()

    # Number of bathrooms e.g. 2
    bathrooms = models.PositiveIntegerField()

    # Property image
    image = models.ImageField(upload_to='properties/')

    # Date created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    