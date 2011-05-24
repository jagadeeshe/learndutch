'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import ModelForm, Textarea, RadioSelect, HiddenInput
from models import Noun, Verb, WORD_TYPE_NOUN, WORD_TYPE_VERB


class NounForm(ModelForm):
    class Meta:
        model = Noun
        widgets = {
            'word_type': HiddenInput(attrs={'value': WORD_TYPE_NOUN}),
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'definite_article': RadioSelect(),
            'indefinite_article': RadioSelect(),
        }

class VerbForm(ModelForm):
    class Meta:
        model = Verb
        widgets = {
            'word_type': HiddenInput(attrs={'value': WORD_TYPE_VERB}),
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'past_perfect_aux': RadioSelect(),
        }
