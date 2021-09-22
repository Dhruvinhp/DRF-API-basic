from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='sungby')
    duration = models.IntegerField()

    def __str__(self):
        return self.title