from django.db import models

class YourModel(models.Model):
    a=models.CharField(max_length=10)
    def __str__(self):
        return self.a