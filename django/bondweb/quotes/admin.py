

# Register your models here.
from django.contrib import admin
from .models import Quote, Author, Category

admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Category)
