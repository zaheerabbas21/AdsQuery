from django.contrib import admin
from Ads.models import Ad, Category, Comment, Fav

# Register your models here.

admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Fav)
