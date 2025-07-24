


# Create your models here.


from django.db import models

# New model for the quote's author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# New model for the quote's category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Updated Quote model
class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'"{self.text[:50]}..." - {self.author.name}'
