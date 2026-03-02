from django.db import models
from django.contrib.auth.models import User

CONDITION_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]

STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]

CATEGORY_CHOICES = [
        ('tops', 'Tops'),
        ('bottoms', 'Bottoms'),
        ('dresses', 'Dresses'),
        ('outerwear', 'Outerwear'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]

SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

class Garment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    story = models.TextField(max_length=250, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    condition = models.IntegerField()
    points_value = models.IntegerField()
    status = models.CharField(max_length=100, default='available')
    listing_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']