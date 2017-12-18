from django.db import models

# Create your models here.


class Blog1(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        # self.str1 = self.author + self.title + self.description
        return self.description
