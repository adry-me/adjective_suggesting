class Setting:
    def __init__(self, filename, exclude_target=None, marker_options=None, special_char=None, special_with_blank=None):
        self.filename = filename
        self.exclude_target = exclude_target if exclude_target is not None else []
        self.marker_options = marker_options if marker_options is not None else {}
        self.special_char = special_char if special_char is not None else []
        self.special_with_blank = special_with_blank if special_with_blank is not None else []


P_P = Setting(
    filename='M_P',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'Pride and Prejudice',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char = ['-', '‘', '.'],
    special_with_blank = ['.', '!', '?', ';', ',', '’', ':']
)

S_S = Setting(
    filename='M_P',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'split': '* * * * *',
        'title': 'Sense and Sensibility',
        'chapter': 'Chapter',
        'website': 'eBook.com',
    },
    special_char = ['-', '‘', '.'],
    special_with_blank = ['.', '!', '?', ';', ',', '’', ':']
)

M_P = Setting(
    filename='M_P',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char = ['-', '‘', '.'],
    special_with_blank = ['.', '!', '?', ';', ',', '’', ':']
)

A_B = Setting(
    filename='A_B',
    exclude_target=['mrs', 'mr', 'ms', 'etc'],
    marker_options={
        'chapter': 'Chapter'
    },
    special_char = ['-', '‘', '.'],
    special_with_blank = ['.', '!', '?', ';', ',', '’', ':']
)