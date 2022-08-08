from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    content = models.TextField()
    datePosted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='img/')

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height >500 or img.width >500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title





