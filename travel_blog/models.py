from django.db import models

class TravelPoint(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    x = models.IntegerField()  # X-координата на карте (в %)
    y = models.IntegerField()  # Y-координата на карте (в %)

    def __str__(self):
        return self.title