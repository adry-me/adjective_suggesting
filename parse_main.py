# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:46:18 2020

@author: Audrey Shin
"""

from concatenate import concatenate
from find_markers import get_markers
from remove_special import remove_special
from merge_lines import merge


def parse(filename, exclude_target: list, marker_options: dict, special_char, special_with_blank, save=False,  save_path=None):
    lines = load_file(filename)
    markers = get_markers(lines, **marker_options)
    lines = concatenate(lines, markers)

    for marker in markers:
        lines.pop(marker)

    lines = merge(lines, exclude_target)
    lines = remove_special(lines, special_char, special_with_blank)

    if save and save_path is not None:
        with open(save_path, 'w') as f:
            for line in lines:
                f.write(f'{line}\n')

    return lines


def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = list(map(str.rstrip, lines))
    lines = list(map(str.lower, lines))

    return lines


if __name__ == '__main__':
    from data.settings import T_TC as SETTING
    contents = parse(f'data/{SETTING.filename}.txt',
                     SETTING.exclude_target,
                     SETTING.marker_options,
                     SETTING.special_char,
                     SETTING.special_with_blank,
                     save=True,
                     save_path=f'data/{SETTING.filename}_mod.txt'
                     )

    for content in contents:
        print(content)