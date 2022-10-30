from django.db import models

# Create your models here.


class Book(models.Model):
    name_of_uploader = models.CharField(max_length=200)
    author_of_book = models.CharField(max_length=100)
    title_of_book = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title_of_book
