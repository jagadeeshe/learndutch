'''
Created on May 18, 2011

@author: jagadeesh
'''
from django import template
from learndutch.mainapp import menu

register = template.Library()

def main_menu():
    items = [ {'label': label, 'link': link } for label, link in menu.main_menu ]
    return {"menu_items": items}

register.inclusion_tag('mainapp/main_menu.html')(main_menu)