'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import ModelForm
from models import Noun, Verb


class NounForm(ModelForm):
    class Meta:
        model = Noun

class VerbForm(ModelForm):
    class Meta:
        model = Verb
