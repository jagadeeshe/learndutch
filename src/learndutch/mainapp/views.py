from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from forms import NounForm, VerbForm, SentenceForm, TagForm, TagObjectForm, WordForm, PageForm, AdjectiveForm
from models import Word, Sentence, Tag, WORD_TYPE_NOUN, WORD_TYPE_VERB, TagObject, WORD_TYPE_PLAIN, Page, WORD_TYPE_ADJECTIVE
from learndutch.mainapp.utils import CustomDetailView, JSONResponseMixin
from learndutch.mainapp.models import WORD_TYPE_PREPOSITION

class CreateNounView(CreateView):
    form_class = NounForm
    template_name = "noun_form.html"
    success_url = "/add-noun/"
    initial = {'word_type': WORD_TYPE_NOUN}

    @method_decorator(permission_required('mainapp.add_noun'))
    def dispatch(self, *args, **kwargs):
        return super(CreateNounView, self).dispatch(*args, **kwargs)


class CreateVerbView(CreateView):
    form_class = VerbForm
    template_name = "verb_form.html"
    success_url = "/add-verb/"
    initial = {'word_type': WORD_TYPE_VERB}

    @method_decorator(permission_required('mainapp.add_verb'))
    def dispatch(self, *args, **kwargs):
        return super(CreateVerbView, self).dispatch(*args, **kwargs)


class CreateAdjectiveView(CreateView):
    form_class = AdjectiveForm
    template_name = "adjective_form.html"
    success_url = "/add-adjective/"
    initial = {'word_type': WORD_TYPE_ADJECTIVE}

    @method_decorator(permission_required('mainapp.add_verb'))
    def dispatch(self, *args, **kwargs):
        return super(CreateAdjectiveView, self).dispatch(*args, **kwargs)


class CreateWordView(CreateView):
    form_class = WordForm
    template_name = "word_form.html"
    success_url = "/add-word/"
    initial = {'word_type': WORD_TYPE_PLAIN}

    @method_decorator(permission_required('mainapp.add_word'))
    def dispatch(self, *args, **kwargs):
        return super(CreateWordView, self).dispatch(*args, **kwargs)


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
        if word.is_adjective:
            self.template_name = 'adjective_form.html'
            self.form_class = AdjectiveForm
            return word.adjective
        self.template_name = 'word_form.html'
        self.form_class = WordForm
        return word

    @method_decorator(permission_required('mainapp.edit_word'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateWordView, self).dispatch(*args, **kwargs)


class WordListView(ListView):
    queryset = Word.objects.extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 20


class VerbListView(ListView):
    queryset = Word.objects.filter(word_type=WORD_TYPE_VERB).extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 20


class NounListView(ListView):
    queryset = Word.objects.filter(word_type=WORD_TYPE_NOUN).extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 20


class AdjectiveListView(ListView):
    queryset = Word.objects.filter(word_type=WORD_TYPE_ADJECTIVE).extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 20


class PrepositionListView(ListView):
    queryset = Word.objects.filter(word_type=WORD_TYPE_PREPOSITION).extra(order_by=['word'])
    template_name = "word_list.html"
    paginate_by = 20


class CreateSentenceView(JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        form = SentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save()
            return self.render_success("done", sentence.sentence)
        else:
            return self.render_error("unknown error")

    @method_decorator(permission_required('mainapp.add_sentence'))
    def dispatch(self, *args, **kwargs):
        return super(CreateSentenceView, self).dispatch(*args, **kwargs)


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
        return self.render_success('done', {'tag':tagname, 'url': tag.get_absolute_url()})

    @method_decorator(permission_required('mainapp.add_tag'))
    def dispatch(self, *args, **kwargs):
        return super(CreateTagView, self).dispatch(*args, **kwargs)


class CreatePageView(CreateView):
    form_class = PageForm
    template_name = "page_form.html"

    @method_decorator(permission_required('mainapp.add_page'))
    def dispatch(self, *args, **kwargs):
        return super(CreatePageView, self).dispatch(*args, **kwargs)


class PageView(DetailView):
    template_name = "page.html"
    slug_field = "name"
    model = Page


class HiddenPageView(DetailView):
    template_name = "page.html"
    slug_field = "name"
    model = Page

    @method_decorator(permission_required('mainapp.view_hidden_page'))
    def dispatch(self, *args, **kwargs):
        return super(HiddenPageView, self).dispatch(*args, **kwargs)


class UpdatePageView(UpdateView):
    slug_field = 'name'
    model = Page
    form_class = PageForm
    template_name = "page_form.html"

    @method_decorator(permission_required('mainapp.edit_page'))
    def dispatch(self, *args, **kwargs):
        return super(UpdatePageView, self).dispatch(*args, **kwargs)


class PageListView(ListView):
    queryset = Page.objects.extra(order_by=['name'])
    template_name = "page_list.html"
    paginate_by = 15

    @method_decorator(permission_required('mainapp.view_list_page'))
    def dispatch(self, *args, **kwargs):
        return super(PageListView, self).dispatch(*args, **kwargs)
