#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Arulalan.T <arulalant@gmail.com>
# 
# This file is part of 'txt2ipa' package examples
# 


from kannada2ipa import kannada2ipa

infile = 'example_sentences_kannada.txt'
outfile = 'example_sentences_ipa.txt'
inf = open(infile, 'r')
outf = open(outfile, 'w')

BUF_SIZE = 100
bcount = 0
tmp_lines = inf.readlines(BUF_SIZE)
while tmp_lines:
    outf.write(kannada2ipa(tmp_lines))	
    tmp_lines = inf.readlines(BUF_SIZE)
    bcount += 100
inf.close()
outf.close()
print "input unicode text '%s'" % infile
print "after ipa file stored in '%s'" % outfile


