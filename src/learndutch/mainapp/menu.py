'''
Created on May 18, 2011

@author: jagadeesh
'''

main_menu = (
    ('Home', '/', None),
    ('Add noun', '/add-noun/', 'mainapp.add_noun'),
    ('Add verb', '/add-verb/', 'mainapp.add_verb'),
    ('Add adjective', '/add-adjective/', 'mainapp.add_adjective'),
    ('Add word', '/add-word/', 'mainapp.add_word'),
    ('Add page', '/add-page/', 'mainapp.add_page'),
    ('Verbs', '/words/verbs/', None),
    ('Nouns', '/words/nouns/', None),
    ('Adjectives', '/words/adjectives/', None),
    ('Prepositions', '/words/prepositions/', None),
    ('All words', '/words/', None),
    ('All pages', '/pages/', 'mainapp.view_list_page'),
)