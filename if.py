#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
s =80.5/(1.75*1.75)
BMI = int(s)
if BMI<18.5:
  print('过轻')
elif BMI>=18.5 and BMI<25:
  print('正常')
elif BMI>=25 and BMI<28:
  print('过重')
elif BMI>=28 and BMI<32:
  print('肥胖')
elif BMI>=32:
  print('严重肥胖')