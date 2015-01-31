from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import generator

def getImage(request):
    #generating a random genome
    genome = generator.generate_new_genome()

    return HttpResponse(generator.generate_image(genome))
