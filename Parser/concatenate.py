# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:42:01 2020

@author: Audrey Shin
"""

def concatenate(lines, markers):
    for marker in markers:
        if marker == 0 or marker == len(lines) - 1:
            continue
        
        prev = lines[marker - 1].split()
        post = lines[marker + 1].split()
        
        if len(prev) > 0 and prev[-1][-1] == '-' and len(post) > 0:
            prev[-1] = prev[-1][:-1] + post[0]
            post.pop(0)
            
            lines[marker - 1] = ' '.join(prev)
            lines[marker + 1] = ' '.join(post)
            
    return lines