from django.contrib import admin
from apps.blog import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
