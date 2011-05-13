'''
Created on May 13, 2011

@author: jagadeesh
'''


# Specify abosolute path where the project is deployed
DEPLOY_ROOT = ''

def get_full_path(name):
    return "%s%s" % (DEPLOY_ROOT, name)