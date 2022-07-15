from django.contrib import admin
from django.contrib import admin
from ecommerce.models import Category, Book, Product, Cart
from store.models import Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Post)