from django.db import models

# Create your models here.

class PythowaKlasa:
    a = 1
    b = 2

    def cos_tam(cls):
        return "xyz"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    on_shelf = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} - {self.author}"