#!/usr/bin/env python3

import io
import os
import time
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader

# make the live web directory if needed
# move old to a timestamp just in case
liveweb = './live'

if os.path.exists(liveweb):
    timestamp = time.strftime('%c').replace(' ', '-').replace(':', '.')
    shutil.move(liveweb, liveweb+'-'+timestamp)

os.makedirs(liveweb)

# parse, render each template here
env = Environment(loader=FileSystemLoader('./'))
files = ['_index.html']


# now render the pages
for f in files:
    template_vars = {}

    html = env.get_template(f).render(template_vars)
    with io.open(os.path.join('./live/', f[1:]), 'w', encoding='utf8') as fout:
        fout.write(html)

# copy these directories as-is to the webdir
livedirs = ['font-awesome', 'bootstrap', 'css', 'images']
for d in livedirs:
    if os.path.isdir(d):
        shutil.copytree(d, os.path.join(liveweb, d))

# copy these files as-is to the webdir
# livefiles = ['robots.txt']
livefiles = []
for f in livefiles:
    shutil.copyfile(f, os.path.join(liveweb, f))
