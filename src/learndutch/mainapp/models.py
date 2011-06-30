from django.db import models

WORD_TYPE_NOUN = 1
WORD_TYPE_VERB = 2
WORD_TYPE_PLAIN = 3

def lookup_value(choices, key, default='?'):
    for k, v in choices:
        if k == key and v == '/': return ''
        if k == key: return v
    return default

def get_formatted(value, format, ifnone='?'):
    if value:
        return format % value
    else:
        return ifnone

class Word(models.Model):
    word_type = models.IntegerField(blank=True)
    word = models.CharField(max_length=255, unique=True)
    meaning = models.CharField(max_length=255, null=True, blank=True)
    info = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='word-image', null=True, blank=True)
    audio = models.FileField(upload_to='word-sound', null=True, blank=True)
    
    @property
    def is_noun(self):
        return self.word_type == WORD_TYPE_NOUN

    @property
    def is_verb(self):
        return self.word_type == WORD_TYPE_VERB

    def get_meaning(self):
        return get_formatted(self.meaning, '- %s', '')

    def get_absolute_url(self):
        return '/word/%s/' % self.word

    def get_edit_url(self):
        return self.get_absolute_url() + "edit/"

    def get_word(self):
        return self.word

class Noun(Word):
    DEFINITE_ARTICLE_CHOICES = (
        (1, 'de'),
        (2, 'het'),
        (3, '/'),
    )
    INDEFINITE_ARTICLE_CHOICES = (
        (1, 'een'),
        (2, '/'),
    )
    definite_article = models.IntegerField(null=True, blank=True, choices=DEFINITE_ARTICLE_CHOICES)
    indefinite_article = models.IntegerField(null=True, blank=True, choices=INDEFINITE_ARTICLE_CHOICES)
    plural = models.CharField(max_length=255, null=True, blank=True)
    diminutive = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_singular(self):
        article = lookup_value(Noun.DEFINITE_ARTICLE_CHOICES, self.definite_article)
        return '%s %s' % (article, self.word)

    @property
    def get_plural(self):
        if self.definite_article == 3:
            return self.plural
        else:
            return get_formatted(self.plural, 'de %s')

    @property
    def get_indefinite_singular(self):
        article = lookup_value(Noun.INDEFINITE_ARTICLE_CHOICES, self.indefinite_article)
        return '%s %s' % (article, self.word)

    @property
    def get_indefinite_plural(self):
        return get_formatted(self.plural, '%s')

    @property
    def get_diminutive(self):
        return get_formatted(self.diminutive, 'het %s')

    def get_word(self):
        return self.get_singular()


class Verb(Word):
    PAST_PERFECT_AUX_CHOICES = (
        (1, 'hebben'),
        (2, 'zijn'),
    )
    present_1st = models.CharField(max_length=255, null=True, blank=True)
    present_2nd = models.CharField(max_length=255, null=True, blank=True)
    present_3rd = models.CharField(max_length=255, null=True, blank=True)
    past_singular = models.CharField(max_length=255, null=True, blank=True)
    past_plural = models.CharField(max_length=255, null=True, blank=True)
    past_perfect_aux = models.IntegerField(null=True, blank=True, choices=PAST_PERFECT_AUX_CHOICES)
    past_perfect = models.CharField(max_length=255, null=True, blank=True)

    def get_past_perfect_aux(self):
        return lookup_value(Verb.PAST_PERFECT_AUX_CHOICES, self.past_perfect_aux)


class Sentence(models.Model):
    ref_word = models.ForeignKey(Word)
    sentence = models.CharField(max_length=10240, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def get_absolute_url(self):
        return '/tag/%s/' % self.name


class TagObject(models.Model):
    tag_name = models.ForeignKey(Tag)
    object_name = models.ForeignKey(Word)
    
    class Meta:
        unique_together = ("tag_name", "object_name")


class Page(models.Model):
    name = models.CharField(max_length=512, unique=True)
    content = models.CharField(max_length=10240)
    
    class Meta:
        permissions = (
            ('view_list', "Can view Page list"),
            ('view_hidden', "Can view hidden Page"),
        )
    
    def get_absolute_url(self):
        return "/page/%s/" % self.name
    
    def get_edit_url(self):
        return self.get_absolute_url() + "edit/"
