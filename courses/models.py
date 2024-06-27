from django.db import models


class Course(models.Model):
    platform = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    price = models.CharField(max_length=50)
    rating = models.FloatField()

    def __str__(self):
        return self.title
