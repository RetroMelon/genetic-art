from django.db import models
import generator

# Create your models here.
class Image(models.Model):
    pass
    #date/time - the date/time this image was created
    created_datetime = models.DateTimeField(auto_now_add = True)

    #genome - the geome that the image is generated from.
    genome = models.CommaSeparatedIntegerField(max_length=generator.GENETIC_CODE_LENGTH)

    #generation - the generation number that the image is from
    generation = models.IntegerField(default=0)

    #popularity - how popular the image is. 0 is default, lower is better
    popularity = models.IntegerField(default=0)

    #parents - many to many with image.
    parents = models.ManyToManyField("Image", blank=True)

    def __unicode__(self):
        return 'Image ' + str(self.id)
