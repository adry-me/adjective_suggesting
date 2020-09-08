# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:12:58 2020

@author: Daniel Shin
"""


def remove_special(lines, special, special_blank):
    for i, line in enumerate(lines):
        words = line.split()
        for target in special:
            words = _search_and_replace(words, target)
        for target in special_blank:
            words = _search_and_replace(words, target, True)
        lines[i] = ' '.join(words)

    return lines


def _search_and_replace(words, target_list, req_blank=False):
    for i, word in enumerate(words):
        for target in target_list:
            if target in word:
                index = word.find(target)
                if req_blank and (index == len(word) - 1 or word[index + 1] == ' '):
                    words[i] = word.replace(target, ' ')
                else:
                    words[i] = word.replace(target, ' ')
                    
    return words
