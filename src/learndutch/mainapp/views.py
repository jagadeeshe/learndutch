from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.generic import CreateView, DetailView

from forms import NounForm, VerbForm
from models import Word


class CreateNounView(CreateView):
    form_class = NounForm
    template_name = "add_noun.html"
    success_url = "/word/add-noun/"


class CreateVerbView(CreateView):
    form_class = VerbForm
    template_name = "add_verb.html"
    success_url = "/word/add-verb/"


class WordView(DetailView):
    template_name = "word.html"
    slug_field = "word"
    model = Word

