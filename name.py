#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
def normalize(name):
  name = name[0].upper()+name[1:].lower()
  return name 
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)