from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=512)
    location = models.CharField(max_length=1024)
    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=512)
    question = models.TextField()
    agree_privacy = models.BooleanField()

    def __str__(self):
        return f'{self.full_name} >> {self.email}'
