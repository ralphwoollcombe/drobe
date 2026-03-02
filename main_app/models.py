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
        ('gifted', 'Gifted')
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

LISTING_TYPE_CHOICES = [
        ('gift', 'Gift'),
        ('lend', 'Lend'),
        ('both', 'Both'),
    ]

POINTS = {
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 11
}

class Garment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    story = models.TextField(max_length=250, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES)
    condition = models.IntegerField(choices=CONDITION_CHOICES)
    points_value = models.IntegerField(editable=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='available')
    listing_type = models.CharField(max_length=100, choices=LISTING_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'garments'

    def save(self, *args, **kwargs):
        self.points_value = POINTS.get(self.condition, 0)
        super().save(*args, **kwargs)