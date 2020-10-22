# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:46:18 2020

@author: Audrey Shin
"""

from Parser.concatenate import concatenate
from Parser.find_markers import get_markers
from Parser.remove_special import remove_special
from Parser.merge_lines import merge


def parse(filename, exclude_target: list, marker_options: dict, special_char, special_with_blank, save=False,  save_path=None, encoding='utf-8'):
    lines = load_file(filename, encoding)
    markers = get_markers(lines, **marker_options)
    lines = concatenate(lines, markers)

    for marker in markers:
        lines.pop(marker)

    lines = merge(lines, exclude_target)
    lines = remove_special(lines, special_char, special_with_blank)

    if save and save_path is not None:
        with open(save_path, 'w', encoding=encoding) as f:
            for line in lines:
                f.write(f'{line}\n')

    return lines


def load_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as f:
        lines = f.readlines()

    lines = list(map(str.rstrip, lines))
    lines = list(map(str.lower, lines))

    return lines


if __name__ == '__main__':
    import os
    import data.settings as settings
    import string

    authors = [d for d in os.listdir('data')
               if os.path.isdir(f'data/{d}')
               and d[0] not in ['.', '_']]
    for author in authors:
        for fname in os.listdir(f'data/{author}'):
            if fname == 'Hamlet.txt':
                SETTING = getattr(settings, fname.split('.txt')[0], None)
                file_path = 'data/Kafka/T_Tr.txt'

                print(f'{SETTING} {fname}')

                if SETTING is not None and os.path.exists(f'{file_path}'):
                    SETTING.special_char.extend(list(string.punctuation))
                    SETTING.special_char.extend('—')
                    contents = parse(f'{file_path}',
                                     SETTING.exclude_target,
                                     SETTING.marker_options,
                                     SETTING.special_char,
                                     SETTING.special_with_blank,
                                     save=True,
                                     save_path=f'data/Kafka/T_Tr_mod.txt',
                                     encoding=SETTING.encoding
                                     )

                    for con in contents:
                        print(con)
            else:
                continue
