from django.contrib import admin
from models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):

    list_display = ('__unicode__', 'generation', 'popularity')

#registering the image model.
admin.site.register(Image, ImageAdmin)
