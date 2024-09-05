from django.db import models

# Create your models here.
class Message(models.Model):
    full_name= models.CharField(blank=False, null=False, max_length=1000)
    phone_number= models.CharField(blank=False, null=False, max_length=20)
    email= models.EmailField()
    message= models.TextField()

    def __str__(self):
        return self.full_name