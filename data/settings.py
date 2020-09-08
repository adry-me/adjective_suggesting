class Setting:
    def __init__(self, filename, exclude_target=None, marker_options=None,
                 special_char=None, special_with_blank=None, encoding=None):
        self.filename = filename
        self.exclude_target = exclude_target if exclude_target is not None else []
        self.marker_options = marker_options if marker_options is not None else {}
        self.special_char = special_char if special_char is not None else []
        self.special_with_blank = special_with_blank if special_with_blank is not None else []
        self.encoding = encoding if encoding is not None else 'utf-8'


P_P = Setting(
    filename='P_P',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'Pride and Prejudice',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char=['—', '‘', '.', '“', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

S_S = Setting(
    filename='S_S',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'Sense and Sensibility',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char=['-', '‘', '.', '—', ';—', '“', '’', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

M_P = Setting(
    filename='M_P',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', ';—', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '"']
)

Emma = Setting(
    filename='Emma',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter',
        'volume': 'Volume'
    },
    special_char=['-', '‘', '.', '“', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '—']
)

W_P1 = Setting(
    filename='W_P1',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'book': 'Book',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '—', '(', ')', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', ')', '—', '”', '"']
)

W_P2 = Setting(
    filename='W_P2',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'book': 'Book',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '—', '(', ')', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', ')', '—', '”', '"']
)

W_P3 = Setting(
    filename='W_P3',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'book': 'Book',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '—', '(', ')', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', ')', '—', '”', '"']
)

W_P4 = Setting(
    filename='W_P4',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'book': 'Book',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '—', '(', ')', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', ')', '—', '”', '"']
)

W_P5 = Setting(
    filename='W_P5',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'book': 'Book',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '—', '(', ')', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', ')', '—', '”', '"']
)

A_K1 = Setting(
    filename='A_K1',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '—']
)

A_K2 = Setting(
    filename='A_K2',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '—']
)

A_K3 = Setting(
    filename='A_K3',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '—']
)

A_K4 = Setting(
    filename='A_K4',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '—']
)

Meta = Setting(
    filename='Meta',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'The Metamorphosis',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char=['-', '‘', '.', '“'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

Sh_St = Setting(
    filename='Sh_St',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'page': 'Page',
        'chapter': 'Chapter',
        'translation': 'Translated by'
    },
    special_char=['-', '‘', '.', '“', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '"']
)

Amerika = Setting(
    filename='Amerika',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'translation': 'Translated by'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”'],
    encoding='latin-1'
)

T_C = Setting(
    filename='T_C',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '"']
)

L_F = Setting(
    filename='L_F',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-', '—', '"'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '"']
)

M_ND = Setting(
    filename='M_ND',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

Hamlet = Setting(
    filename='Hamlet',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

K_L = Setting(
    filename='K_L',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

Macbeth = Setting(
    filename='Macbeth',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

R_J = Setting(
    filename='R_J',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

Othello = Setting(
    filename='Othello',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'act': 'ACT',
        'scene': 'Scene',
        'enter': 'Enter',
        'exit': 'Exit',
        'exeunt': 'Exeunt',
        'chapter': 'Chapter'
    },
    special_char=['‘', '.', '“', '.', '!', '?', ',', '-'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”']
)

O_T = Setting(
    filename='O_T',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'The Metamorphosis',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char=['-', '‘', '.', '“'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '']
)

G_E = Setting(
    filename='G_E',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'The Metamorphosis',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char=['-', '‘', '.', '“', '(', ')'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '', '(', ')']
)

C_C = Setting(
    filename='C_C',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'stave': 'STAVE',
        'title': 'A CHRISTMAS CAROL'
    },
    special_char=['-', '‘', '.', '“'],
    special_with_blank=['.', '!', '?', ';', ',', '’', '”', ':']
)

T_TC = Setting(
    filename='T_TC',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'title': 'A T A L E O F T W O C I T I E S',
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.', '“', '(', ')', '—'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':', '”', '(', ')', '—']
)

A_B = Setting(
    filename='A_B',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char=['-', '‘', '.'],
    special_with_blank=['.', '!', '?', ';', ',', '’', ':']
)