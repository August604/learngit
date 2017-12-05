#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
def is_palindrome(n):
  s = str(n)
  if len(s)==1:
    return True
  else:
    list=[c for c in s]
    new_list=[]
    for x in range (len(list)):
      new_list.append(list[len(list)-x-1])
    if (''.join(new_list))==s:
      return True
    else:
      return False
output = filter(is_palindrome,range(1,1000))
print(list(output))
