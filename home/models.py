from django.db import models

# Create your models here.
class Contact(models.Model):
    FullName = models.CharField(max_length=20)
    emailInfo = models.EmailField()
    phone = models.IntegerField()
    desc = models.TextField(max_length=100)
    def __str__(self):
        return self.FullName
