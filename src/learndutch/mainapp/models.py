from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)
    meaning = models.CharField(max_length=255, null=True)
    info = models.CharField(max_length=1024, null=True)


class Noun(Word):
    DEFINITE_ARTICLE_CHOICES = (
        (0, ''),
        (1, 'de'),
        (2, 'het'),
    )
    INDEFINITE_ARTICLE_CHOICES = (
        (0, ''),
        (1, 'een'),
        (2, '--'),
    )
    definite_article = models.IntegerField(choices=DEFINITE_ARTICLE_CHOICES)
    indefinite_article = models.IntegerField(choices=INDEFINITE_ARTICLE_CHOICES)
    plural = models.CharField(max_length=255, null=True)
    diminutive = models.CharField(max_length=255, null=True)


class Verb(Word):
    present_1st = models.CharField(max_length=255, null=True)
    present_2nd = models.CharField(max_length=255, null=True)
    present_3rd = models.CharField(max_length=255, null=True)
    past_1st = models.CharField(max_length=255, null=True)
    past_2nd = models.CharField(max_length=255, null=True)
    past_3rd = models.CharField(max_length=255, null=True)
    past_plural = models.CharField(max_length=255, null=True)
    past_perfect_1st = models.CharField(max_length=255, null=True)
    past_perfect_2nd = models.CharField(max_length=255, null=True)
    past_perfect_3rd = models.CharField(max_length=255, null=True)
    past_perfect_plular = models.CharField(max_length=255, null=True)


class Sentence(models.Model):
    ref_word = models.ForeignKey(Word)
    sentence = models.CharField(max_length=1024)


class Tag(models.Model):
    name = models.CharField(max_length=75)


class TagObject(models.Model):
    tag_name = models.ForeignKey(Tag)
    object_name = models.ForeignKey(Word)

