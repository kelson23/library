from django.db import models
from uuid import uuid4

# Create your models here.

class Category(models.Model):
    idCategory = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)

class Books(models.Model):
    idBook = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, default=None, on_delete = models.CASCADE)
    bookCover = models.ImageField(upload_to='books/static/images/')
    author = models.CharField(max_length=255)
    publishDate = models.DateField()
    pages = models.IntegerField()
    createAt = models.DateField(auto_now_add=True)