from django.db import models
from django.utils import timezone

class Manhwa(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='manhwa_covers/')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Chapter(models.Model):
    manhwa = models.ForeignKey(Manhwa, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='manhwa_chapters/')
    release_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.manhwa.title} - Chapter {self.chapter_number}'