from django.views.generic import CreateView, ListView, UpdateView, View
from django.http import HttpResponse

from forms import NounForm, VerbForm, SentenceForm, TagForm, TagObjectForm, WordForm
from models import Word, Sentence, Tag, WORD_TYPE_NOUN, WORD_TYPE_VERB, TagObject, WORD_TYPE_PLAIN
from learndutch.mainapp.utils import CustomDetailView, JSONResponseMixin

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


class CreateWordView(CreateView):
    form_class = WordForm
    template_name = "word_form.html"
    success_url = "/add-word/"
    initial = {'word_type': WORD_TYPE_PLAIN}


class WordView(CustomDetailView):
    template_name = "word.html"
    slug_field = "word"
    model = Word

    def get_extra_context_data(self):
        return {"setence_form": self.create_sentence_form(),
                "sentence_list": self.get_SentenceList(),
                "tag_form": self.create_tag_form(),
                "tag_list": self.get_tag_list()}

    def create_sentence_form(self):
        form = SentenceForm(initial={'ref_word_id': self.object.id})
        return form

    def get_SentenceList(self):
        q1 = Sentence.objects.filter(ref_word=self.object)
        return q1

    def create_tag_form(self):
        form = TagForm(initial={'object_id': self.object.id})
        return form

    def get_tag_list(self):
        q1 = TagObject.objects.filter(object_name=self.object)
        result = [ tagobj.tag_name for tagobj in q1]
        return result



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
    queryset = Word.objects.extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 15


class CreateSentenceView(JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save()
            return self.render_success("done", sentence.sentence)
        else:
            return self.render_error("unknown error")


class CreateTagView(JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        tag_form = TagForm(request.POST)
        tag_form.is_valid()
        tagname = tag_form.cleaned_data['name']
        tag_count = Tag.objects.filter(name=tagname).count()
        if tag_count == 0:
            tag = tag_form.save()
        else:
            tag = Tag.objects.get(name=tagname)
        tagobjectdata = {'tag_id': tag.id, 'object_id': tag_form.cleaned_data['object_id']}
        tagobject_form = TagObjectForm(tagobjectdata)
        tagobject_form.is_valid()
        tagobject_form.save()
        return self.render_success('done')

