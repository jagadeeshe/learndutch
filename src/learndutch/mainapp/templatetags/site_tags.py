'''
Created on May 18, 2011

@author: jagadeesh
'''
from django import template
from learndutch.mainapp import menu
from django.utils.safestring import mark_safe

register = template.Library()

def main_menu():
    items = [ {'label': label, 'link': link } for label, link in menu.main_menu ]
    return {"menu_items": items}

register.inclusion_tag('components/main_menu.html')(main_menu)


@register.filter
def textile(value):
    from learndutch import textile
    result = textile.textile(value)
    return mark_safe(result)

