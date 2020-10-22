from urllib.request import urlopen
import json


def get_synonyms(entry):
    return _to_synonyms(_crawl_tuna_raw(entry))


def _crawl_tuna_raw(entry):
    url = f'https://tuna.thesaurus.com/pageData/{entry}'
    response = urlopen(url)
    txt = response.read().decode('utf-8')

    obj = json.loads(txt)
    data = obj.get('data')
    if data is None:
        return None

    word_data = data.get('definitionData').get('definitions')
    return word_data


def _to_synonyms(word_data):
    if word_data is None:
        return []

    adj_defs = [d for d in word_data if d.get('pos') == 'adjective']
    synonyms = []
    for d in adj_defs:
        synonyms.extend([s.get('term') for s in d.get('synonyms') if s.get('similarity') == 100])

    return synonyms
