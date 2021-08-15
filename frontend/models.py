from django.db import models

# Create your models here.
class Event(models.Model):
    SEASONS = [
        ('Spring', "Spring"),
        ('Summer', "Summer"),
        ('Fall', "Fall"),
        ('Winter', "Winter"),
    ]
    season=models.CharField(max_length=7, null=False, choices=SEASONS)
    month=models.CharField(max_length=15, null=False, default="January")
    name=models.CharField(max_length=25, null=False)
    details=models.CharField(max_length=100, null=False, default="None")
    betting=models.CharField(max_length=30, null=False, default="Las Vegas/Online")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('season', 'month', 'name', 'details', 'betting', 'created_at', 'updated_at')

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255, null=False)
    header = models.CharField(max_length=255, null=False)
    blog = models.TextField(null=False)
    author = models.TextField(null=False)
    url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', 'header', 'blog', 'author', 'url', 'created_at', 'updated_at')

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    episode=models.CharField(max_length=255)
    video=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', 'title', 'description', 'episode', 'video', 'created_at', 'updated_at')

    def __str__(self):
        return self.title

class Product(models.Model):

    COLORS = [
        ('Black', 'Black'),
        ('White', 'White'),
        ('Grey', 'Grey'),
        ('Red', 'Red'),
        ('Blue', 'Blue')
    ]

    TYPE = [
        ('T-Shirt', 'T-Shirt'),
        ('Long-Sleeve Shirt', 'Long-Sleeve Shirt'),
        ('Sweatshirt', 'Sweatshirt'),
        ('Jacket', 'Jacket'),
        ('Hat', 'Hat'),
    ]

    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    SIZES = [
        ('XS', 'SX'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    ]

    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    image=models.ImageField(upload_to="static/img/products/")
    colors=models.CharField(max_length=255, choices=COLORS, default="White")
    types=models.CharField(max_length=255, choices=TYPE, default="T-Shirt")
    sex=models.CharField(max_length=10, choices=SEX, default="Male")
    sizes=models.CharField(max_length=20, choices=SIZES, default="L")
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', 'name', 'description', 'price', 'image', 'colors', 'types', 'sex', 'sizes', 'quantity', 'created_at', 'updated_at')

    def __str__(self):
        return self.name


