from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.FloatField()
    stock=models.PositiveIntegerField(default=0)
    supplier=models.CharField(max_length=255,blank=True,null=True)
    expiry_date = models.DateField(blank=True, null=True)
    Manufactured_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name