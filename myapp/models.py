from django.db import models

# Create your models here.

class Image(models.Model):
    Name = models.CharField(max_length=100)
    Images = models.ImageField(upload_to="static/picture/")
    
    class Meta:
        db_table = "Image_table"