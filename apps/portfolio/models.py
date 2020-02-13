from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    preview_image = models.FilePathField(path="/img")
    reference_link = models.URLField(max_length=250)

    def __str__(self):
        return self.title