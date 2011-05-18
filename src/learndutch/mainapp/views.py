from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

from forms import NounForm, VerbForm

def add_noun(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.method == "POST":
        form = NounForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/word/add-noun/')
    else:
        form = NounForm()
    ctx['form'] = form
    return render_to_response('add_noun.html', ctx)


def add_verb(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.method == "POST":
        form = VerbForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/word/add-verb/')
    else:
        form = VerbForm()
    ctx['form'] = form
    return render_to_response('add_verb.html', ctx)