'''
Created on May 18, 2011

@author: jagadeesh
'''
from django import template
from learndutch.mainapp import menu
from django.utils.safestring import mark_safe
from learndutch.mainapp.models import Page

register = template.Library()

def main_menu(user):
    items = []
    for label, link, perm in menu.main_menu:
        if perm == None or user.has_perm(perm):
            items.append({'label': label, 'link': link })
    return {"menu_items": items}

register.inclusion_tag('components/main_menu.html')(main_menu)


@register.simple_tag
def page(name):
    'Usage: {% page "_page_name_" %} do not forget to load {% load site_tags %}'
    pg = Page.objects.get(name=name)
    return textile(pg.content)



@register.filter
def textile(value):
    from learndutch import textile
    result = textile.textile(value)
    return mark_safe(result)

