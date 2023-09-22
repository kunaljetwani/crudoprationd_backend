from django.db import models

# Create your models here.


class book (models.Model):
    tittle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()


class rating (models.Model):

    rate = models.DecimalField(decimal_places=2, max_digits=3)
    count = models.DecimalField(decimal_places=3, max_digits=4)


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    Description = models.CharField(max_length=300)
    Price = models.IntegerField()
    Image = models.CharField(max_length=300)
    rating = models.FloatField()    


class order(models.Model):
    order_id = models.IntegerField(unique=True)
    list_of_products = models.ManyToManyField(product)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    subtotal = models.DecimalField(max_digits=4, decimal_places=2)

# class product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=300)
#     Description = models.CharField(max_length=300)
#     Price = models.IntegerField()
#     Category=models.IntegerField()
#     Image = models.CharField(max_length=300)
#     rating = models.DecimalField(max_digits=10,decimal_places=3)


# class Category (models.Model):
#     name=models.CharField(max_length=200)
