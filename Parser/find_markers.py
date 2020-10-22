# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:31:49 2020

@author: Audrey Shin
"""

def get_markers(lines, **kwargs):
    markers = []
    
    for key in kwargs:
        for i, line in enumerate(lines):
            if kwargs.get(key).lower() in line:
                markers.append(i)
                
    markers.sort(reverse=True)
    return markers


if __name__ == '__main__':
    with open('../data/Austen/P_P.txt') as f:
        lines = f.readlines()
        
    lines = list(map(str.rstrip, lines))

    markers = get_markers(lines,
                          title = 'Sense and Sensibility',
                          chapter_style = 'Chapter', 
                          website = 'Free eBooks at Planet eBook.com')
    
    for marker in markers:
        print(lines[marker])