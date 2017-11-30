#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
def MM(L):
  if MM(L)==0:
    return (none,none)
  else:
   a=L[0]
   b=L[0]
   for x in L:
     if a>=x:
       a = x
     if b <=x:
       b=x
   return(a,b)
L=[1,2,3,4,5]
print(MM(L))