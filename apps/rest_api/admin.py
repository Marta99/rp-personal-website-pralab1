from django.contrib import admin
from . import models

# Register your models here.
# New way---------------------------------------
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
# Old way --------------------------------------
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Comment, CommentAdmin)