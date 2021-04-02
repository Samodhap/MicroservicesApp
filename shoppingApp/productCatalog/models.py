from django.db import models


# Create your models here.
class Products(models.Model):
    product_serial_num = models.CharField(max_length=20,primary_key=True)
    product_name = models.CharField(max_length=30)
    price = models.FloatField()
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.product_serial_num
