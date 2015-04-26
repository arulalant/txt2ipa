#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# 
# This file is part of 'txt2ipa' package examples
# 


from kannada2ipa import kannada2ipa

text = '﻿ಇವತ್ತಿನ ಹವಾಮಾನ ಚನ್ನಾಗಿದೆ'


print "input unicode text", text
print "after ipa", kannada2ipa(text)


