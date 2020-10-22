import os


_encoding = 'utf-8'
_object = {}
_path = 'data'
_object_fname = 'words.bytes'


def set_path(path):
    global _path
    _path = path


def encode(suffix='_mod'):
    import os

    authors = [d for d in os.listdir(f'{_path}')
               if os.path.isdir(f'{_path}/{d}')
               and d[0] not in ['.', '_']]
    print(authors)
    for author in authors:
        result = {}
        print(author)
        for fname in [f'{_path}/{author}/{fn}' for fn in os.listdir(f'{_path}/{author}') if suffix in fn]:
            with open(fname, encoding=_encoding) as f:
                try:
                    for line in f.readlines():
                        line = line.rstrip()

                        for word in line.split():
                            if word not in result:
                                result[word] = 0
                            result[word] += 1
                except UnicodeDecodeError as e:
                    print(f'{fname} - UNICODE ERROR {e}')
                    raise e
            print(f'{fname} done')

        print(len(result))

        with open(f'{_path}/{author}/{len(result)}-{_object_fname}', 'wb') as f:
            for word in result:
                f.write(bytes(f'{word} ', encoding=_encoding))

    return result


def decode(target, author):
    if target in _get_object(author):
        return _get_object(author).index(target) + 1
    return 0


def to_word(number, author):
    return _get_object(author)[number - 1]


def _get_object(author):
    global _object

    if _object.get(author) is None:
        tmp_path = os.getcwd()
        f_path = os.path.abspath(os.path.dirname(__file__))
        os.chdir(f_path)
        os.chdir('..')

        fnames = [fname for fname in os.listdir(f'{_path}/{author}')
                  if _object_fname in fname]

        assert(len(fnames) == 1, f'Check words.bytes file in {_path}/{author}')

        with open(f'{_path}/{author}/{fnames[0]}', 'rb') as f:
            data = f.read().decode(encoding=_encoding)
            _object[author] = data.split()
        os.chdir(tmp_path)

    return _object[author]


if __name__ == '__main__':
    obj = encode()

    print(decode('it', 'Austen'))
    print(decode('good', 'Austen'))