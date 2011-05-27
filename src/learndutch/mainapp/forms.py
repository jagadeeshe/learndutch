'''
Created on May 18, 2011

@author: jagadeesh
'''
from django.forms import  ModelForm, Textarea, RadioSelect, HiddenInput
from models import Noun, Verb, Sentence, Tag, TagObject
from django import forms

class NounForm(ModelForm):
    class Meta:
        model = Noun
        widgets = {
            'word_type': HiddenInput(),
            'info': Textarea(attrs={'cols': 50, 'rows': 5}),
            'definite_article': RadioSelect(),
            'indefinite_article': RadioSelect(),
        }

class VerbForm(ModelForm):
    class Meta:
        model = Verb
        widgets = {
            'word_type': HiddenInput(),
            'info': Textarea(attrs={'cols': 50, 'rows': 5}),
            'past_perfect_aux': RadioSelect(),
        }


class SentenceForm(forms.Form):
    ref_word_id = forms.IntegerField(widget=HiddenInput)
    sentence = forms.CharField(max_length=1024, widget=Textarea(attrs={'cols': 50, 'rows': 5}))

    def save(self):
        s = Sentence()
        s.sentence = self.cleaned_data['sentence']
        s.ref_word_id = self.cleaned_data['ref_word_id']
        s.save()
        return s


class TagForm(forms.Form):
    name = forms.CharField(max_length=75)
    object_id = forms.IntegerField(widget=HiddenInput)

    def save(self):
        t = Tag()
        t.name = self.cleaned_data['name']
        t.save()
        return t


class TagObjectForm(forms.Form):
    tag_id = forms.IntegerField()
    object_id = forms.IntegerField(widget=HiddenInput)
    
    def save(self):
        to = TagObject()
        to.tag_name_id = self.cleaned_data['tag_id']
        to.object_name_id = self.cleaned_data['object_id']
        to.save()
        return to
