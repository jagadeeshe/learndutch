from django.views.generic import CreateView, ListView, UpdateView, View
from django.http import HttpResponse

from forms import NounForm, VerbForm, SentenceForm
from models import Word, Sentence, WORD_TYPE_NOUN, WORD_TYPE_VERB
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


class WordView(CustomDetailView):
    template_name = "word.html"
    slug_field = "word"
    model = Word

    def get_extra_context_data(self):
        return {"setence_form": self.create_sentence_form(),
                "sentence_list": self.get_SentenceList()}

    def create_sentence_form(self):
        form = SentenceForm(initial={'ref_word_id': self.object.id})
        return form

    def get_SentenceList(self):
        q1 = Sentence.objects.filter(ref_word=self.object)
        return q1



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


class CreateSentenceView(JSONResponseMixin, View):

    def post(self, request, *args, **kwargs):
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save()
            return self.render_success("done", sentence.sentence)
        else:
            return self.render_error("unknown error")
