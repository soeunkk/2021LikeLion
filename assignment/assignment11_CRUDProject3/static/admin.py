from django.contrib import admin
from .models import Review, Comment, Scrap, Like

# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Scrap)
admin.site.register(Like)