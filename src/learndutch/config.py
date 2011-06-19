'''
Created on May 13, 2011

@author: jagadeesh
'''
import os

def get_full_path(name):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    parts = dir_path.split(os.path.sep)
    deploy_root = os.path.sep.join(parts[:-2])
    return os.path.join(deploy_root, name)