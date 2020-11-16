from django.db import models

# Create your models here.
from django.db import models

class Gallery(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'gallery/', default = 'static/images/default.jpg')