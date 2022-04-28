from django.db import models

class hello(models.Model):
    text = models.TextField(max_length= 255, null = False)