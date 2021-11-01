from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category(), blank=True, null=True, on_delete=models.CASCADE)
    store = models.ForeignKey(Shop(), blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

