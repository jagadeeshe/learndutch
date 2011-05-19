'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import ModelForm, Textarea, RadioSelect
from models import Noun, Verb


class NounForm(ModelForm):
    class Meta:
        model = Noun
        widgets = {
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'definite_article': RadioSelect(),
            'indefinite_article': RadioSelect(),
        }

class VerbForm(ModelForm):
    class Meta:
        model = Verb
        widgets = {
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'past_perfect_aux': RadioSelect(),
        }
