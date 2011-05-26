'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import  ModelForm, Textarea, RadioSelect, HiddenInput
from models import Noun, Verb, Sentence
from django import forms

class NounForm(ModelForm):
    class Meta:
        model = Noun
        widgets = {
            'word_type': HiddenInput(),
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'definite_article': RadioSelect(),
            'indefinite_article': RadioSelect(),
        }

class VerbForm(ModelForm):
    class Meta:
        model = Verb
        widgets = {
            'word_type': HiddenInput(),
            'info': Textarea(attrs={'cols': 40, 'rows': 5}),
            'past_perfect_aux': RadioSelect(),
        }


class SentenceForm(forms.Form):
    ref_word_id = forms.IntegerField(widget=HiddenInput)
    sentence = forms.CharField(max_length=1024, widget=Textarea(attrs={'cols': 40, 'rows': 5}))

    def save(self):
        s = Sentence()
        s.sentence = self.cleaned_data['sentence']
        s.ref_word_id = self.cleaned_data['ref_word_id']
        s.save()
        return s
