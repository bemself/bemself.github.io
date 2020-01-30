# -*- coding: utf-8 -*-
import time
import os, subprocess

import re, shutil, glob

from invoke import task
#from fabric.context_managers import cd
__version__ = 'blog v.20200130.2142'
__author__ = 'Bemself'
__license__ = 'MIT@2020-01'


@task
def git(c):
    subprocess.call(
        'git st'
        '&& git add .'
        '&& git ci -m "add"'
        
        '&& git pl'
        '&& git pu',
        shell=True
    )
