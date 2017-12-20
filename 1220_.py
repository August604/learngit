#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self,name,score):
      self.name = name 
      self.score = score
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa simpson', 87)
print('bart.name =',bart.name)
print('bart.score =',bart.score)