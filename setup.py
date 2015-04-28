#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2014-2015 Arulalan.T
# txt2ipa project

from distutils.core import setup
from codecs import open

setup(name='txt2ipa',
      version='v0.2',
      description='Tamil, Kannda language text unicode to International Phonetic Alphabet (IPA) converters',
      author='Arulalan.T',
      author_email='arulalant@gmail.com',
      url='https://github.com/arulalant/txt2ipa',
      packages=['tamil2ipa', 'kannada2ipa'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers='Natural Language :: Tamil, Kannada',
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arulalant/txt2ipa/archive/master.zip',#pip
      )
