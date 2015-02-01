from django.db import models

# Create your models here.
class Image(models.Model):
    pass
    #date/time - the date/time this image was created
    #genome - the geome that the image is generated from.
    #generation - the generation number that the image is from
    #popularity - how popular the image is. 0 is default, lower is better
    #parents - many to many with image.
