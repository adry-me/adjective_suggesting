# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:31:16 2020

@author: Daniel Shin
"""

def merge(lines, special):
    content = ' '.join(lines)
    lines = content.split('. ')
    
    markers = _get_special_markers(lines, special)
    lines = _recover_special(lines, markers)
    
    return lines
    
    
        
def _get_special_markers(lines, special):
    markers = []
    
    for i, line in enumerate(lines):
        for s in special:
            if s in line:
                markers.append(i)
    
    markers.sort(reverse=True)
    return markers

def _recover_special(lines, markers):
    for marker in markers:
        if marker < len(lines) - 1:
            lines[marker] = lines[marker] + ' ' + lines[marker + 1]
            lines.pop(marker + 1)
            
    return lines