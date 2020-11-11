from django.db import models

class Image(models.Model): ##courtesy of the fine gentlemen at 4chan.org
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, default="static/francis/img/no-image.png")
    author = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    caption = models.CharField(max_length=280) ##hehe twitter joke

    def __str__(self):
        return self.title
# Create your models here.
