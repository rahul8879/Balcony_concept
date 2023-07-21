from django.db import models

# Create your models here.


class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
