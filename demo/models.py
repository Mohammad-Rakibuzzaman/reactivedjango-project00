from django.db import models

# Create your models here.
class Book(models.Model):

    # STATUSES = (
    #     (0, 'Unknown'),
    #     (1, 'processed'),
    #     (2, 'paid')
    # )

    # title = models.CharField(null=True, blank=False, unique=True,
    #                          default='', choices=STATUSES)

    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    # price = models.FloatField(default=0, max_digits=0, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    # price = models.BigIntegerField(default=0)

    # published = models.DateField(auto_now=True, auto_now_add=True)
    # published = models.TimeField(auto_now=True, auto_now_add=True)
    # published = models.DateTimeField(auto_now=True, auto_now_add=True)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    # cover = models.FileField(upload_to='covers')
    cover = models.ImageField(upload_to='covers', blank=True)


