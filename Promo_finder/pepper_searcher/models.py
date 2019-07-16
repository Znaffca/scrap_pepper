from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=80)


class PepperPromo(models.Model):
    fullname = models.CharField(max_length=255)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="category_id"
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    url_link = models.TextField()
    promo_code = models.CharField(max_length=80)
