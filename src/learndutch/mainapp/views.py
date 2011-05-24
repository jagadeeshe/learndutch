from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.generic import CreateView, DetailView, ListView

from forms import NounForm, VerbForm
from models import Word, Noun, Verb


class CreateNounView(CreateView):
    form_class = NounForm
    template_name = "add_noun.html"
    success_url = "/add-noun/"


class CreateVerbView(CreateView):
    form_class = VerbForm
    template_name = "add_verb.html"
    success_url = "/add-verb/"


class WordView(DetailView):
    template_name = "word.html"
    slug_field = "word"
    model = Word


class WordListView(ListView):
    model = Word
    template_name = "word_list.html"
    paginate_by = 15

