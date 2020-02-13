#!/anaconda3/envs/nbbinder/bin/python
# -*- coding: utf-8 -*-
'''
Binds the jupyter notebooks that make up the collection of lecture notes.
'''

import os

import nbbinder as nbb

os.chdir(os.path.dirname(__file__))

nbb.bind('binder_config.yml')