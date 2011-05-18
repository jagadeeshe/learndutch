'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import ModelForm
from models import Noun


class NounForm(ModelForm):
    class Meta:
        model = Noun
