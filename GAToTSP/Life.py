# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:18:42 2017

@author: hjmre
"""

SCORE_NONE = -1

class Life(object):
      """个体类"""
      def __init__(self, aGene = None):
            self.gene = aGene
            self.score = SCORE_NONE
