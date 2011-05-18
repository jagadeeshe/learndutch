from django.shortcuts import render_to_response


def add_noun(request):
    return render_to_response('add_noun.html')

def add_verb(request):
    return render_to_response('add_verb.html')