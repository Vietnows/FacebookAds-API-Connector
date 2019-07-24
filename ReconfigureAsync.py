# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:08:50 2019

@author: marcelo.oliveira
"""

import os, re
path = r"C:/Users/marcelo.oliveira/AppData/Local/Continuum/anaconda3/Lib/site-packages/facebookads"

python_files = []

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".py"):
            python_files.append(os.path.join(dirpath, filename))

for python_file in python_files:

    with open(python_file, "r") as f:
        text = f.read()
        revised_text = re.sub("async", "async_", text)

    with open(python_file, "w") as f:
        f.write(revised_text)