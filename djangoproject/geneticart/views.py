from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import generator



def mainpage(request):
    #we put the ids of images yet to be chosen in the page.
    return render_to_response('main.html', {"images": [1, 2, 3, 4, 5, 6, 7, 8],}, context_instance=RequestContext(request))

def get_image(request):
    #generating a random genome
    genome = generator.generate_new_genome()

    return HttpResponse(generator.generate_image(genome), content_type="image/svg+xml")
