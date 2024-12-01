from django.db import models

# Create your models here.
class History(models.Model):
    image=models.ImageField(upload_to="images/")
    prompt=models.CharField(max_length=100)
    response=models.CharField(max_length=1000,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prompt