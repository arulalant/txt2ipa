#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# Author : Arulalan.T <arulalant@gmail.com>                                  #
# Date : 26.04.2015                                                          #
#                                                                            #
# This file is part of txt2ipa                                               #
#                                                                            #
# txt2ipa is free software: you can redistribute it and/or                   #
# modify it under the terms of the GNU General Public License as published by#
# the Free Software Foundation, either version 3 of the License, or (at your #
# option) any later version. This program is distributed in the hope that it #
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty#
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General#
# Public License for more details. You should have received a copy of the GNU#
# General Public License along with this program. If not, see                #
# <http://www.gnu.org/licenses/>.                                            #
#                                                                            #
##############################################################################

from orddic import OrderedDict
from kannada2ipaMap import kan2ipa 

__all__ = ['kan2ipa', 'kannada2ipa']
    

def unicode2ipa(text, charmap):
    '''
    charmap : dictionary which has both unicode as key, ipa as value
    '''
    if isinstance(text, (list, tuple)):
        unitxt = ''
        for line in text:
            for key,val in charmap.iteritems():
                if key in line:
                    line = line.replace(key, val)
                # end of if key in text:
            unitxt += line
        # end of for line in text:
        return unitxt
    elif isinstance(text, str):
        for key,val in charmap.iteritems():
            if key in text:
                text = text.replace(key, val)
            # end of if key in text:
        # end of for key,val in charmap.iteritems():
        return text
    # end of if isinstance(text, (list, tuple)):
# end of def encode2unicode(text, charmap):

def kannada2ipa(text):
    return unicode2ipa(text, kan2ipa)


