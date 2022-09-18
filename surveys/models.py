from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time',)
