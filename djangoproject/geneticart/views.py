from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import generator



def mainpage(request):

    text_list = ["just arbitrary text", "a lil something something", "wut", "...... ... ...", "hopefully this text will be displayed properly.", "hopefulz"] * 2
    tree_items = []

    for words in text_list:
        tree_items.append({'text':words,})


    #we put the ids of images yet to be chosen in the page.
    return render_to_response('main.html', {'images': [1, 2, 3, 4, 5, 6, 7, 8], 'treeitems':tree_items,}, context_instance=RequestContext(request))

def get_image(request):
    #generating a random genome
    genome = generator.generate_new_genome()

    return HttpResponse(generator.generate_image(genome), content_type='image/svg+xml')
