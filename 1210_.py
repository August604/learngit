#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import time,functools
def metric(fn):
  print('%s executed in %s ms' % (fn.__name__,10.24))
  return fn
  

@metric
def fast(x,y):
  time.sleep(0.0012)
  return x+ y
#f = fast(2,3)  
print(fast(2,3))