from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return self.name
class ot_places(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='other_pics')
    desc1=models.TextField()

    # def __str__(self):
    #     return self.name1