from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.generic import CreateView, DetailView, ListView

from forms import NounForm, VerbForm
from models import Word, Noun, Verb, WORD_TYPE_NOUN, WORD_TYPE_VERB


class CreateNounView(CreateView):
    form_class = NounForm
    template_name = "noun_form.html"
    success_url = "/add-noun/"
    initial = {'word_type': WORD_TYPE_NOUN}


class CreateVerbView(CreateView):
    form_class = VerbForm
    template_name = "verb_form.html"
    success_url = "/add-verb/"
    initial = {'word_type': WORD_TYPE_VERB}


class WordView(DetailView):
    template_name = "word.html"
    slug_field = "word"
    model = Word


class WordListView(ListView):
    model = Word
    template_name = "word_list.html"
    paginate_by = 15

