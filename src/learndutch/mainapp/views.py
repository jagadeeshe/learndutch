from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.generic import CreateView, DetailView, ListView, UpdateView

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


class UpdateWordView(UpdateView):
    slug_field = 'word'
    model = Word
    def get_object(self):
        word = UpdateView.get_object(self, queryset=None)
        if word.is_noun:
            self.template_name = 'noun_form.html'
            self.form_class = NounForm
            return word.noun
        if word.is_verb:
            self.template_name = 'verb_form.html'
            self.form_class = VerbForm
            return word.verb
        raise Exception('unknown word type')


class WordListView(ListView):
    model = Word
    template_name = "word_list.html"
    paginate_by = 15

