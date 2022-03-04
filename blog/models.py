from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
#    date = models.DateField(auto_now_add=True)
    description = models.TextField()
#    url = models.URLField(blank=True)
