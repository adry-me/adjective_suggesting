import json
import string

from django.http import HttpResponse
from django.shortcuts import render
from .models import Adjective
from .create_dictionary import save, create_synonyms
import os
from pathlib import Path
import sys
root = Path(__file__).parent.parent.parent

sys.path.append(os.path.dirname(
    os.path.abspath(
        os.path.dirname(
            os.path.abspath(
                os.path.dirname(
                    __file__
                )
            )
        )
    )
))
import main
from nlp.synonymgenerator import SynonymGenerator
from .model.w2v_suggest import most_similar


# Create your views here.
def sample(request):
    return render(request, 'SuggestAdjectives/sample.html')


def input_contents(request):
    return render(request, 'SuggestAdjectives/input_contents.html')


def select_words(request):
    if request.method == 'GET':
        raw_lines = ['He is a good and nice guy', 'She is a kind and compassionate girl, one of the best people I have ever met in my life']
    else:
        input_text_raw = request.POST.get('input-text')
        raw_lines = list(map(str.rstrip, input_text_raw.split('\n')))

    authors = get_author_names()

    lines = []
    for line in raw_lines:
        for p in string.punctuation:
            line = line.replace(p, '')
        lines.append(line.lower())

    return render(request, 'SuggestAdjectives/select_words.html', {
        'lines': lines,
        'authors': authors
    })


def suggest(request):
    original_lines = []
    similar_sentences = {}
    generated_sentences = {}
    if request.method == 'POST':
        selected = json.loads(request.POST.get('selected-words'))
        authors = [author for author in get_author_names()
                   if request.POST.get(author) is not None]

        lines = selected.keys()

        os.chdir(root)
        syn_gen_list = []

        for line in lines:
            adj_list = selected[line]

            for adj in adj_list:
                adj_objects = Adjective.objects.filter(word=adj)
                if len(adj_objects) > 0:
                    adj_object = adj_objects[0]
                    adj_word = adj_object.word
                    synonyms = []
                    similar_words = []
                    for author in authors:
                        sim_words = most_similar(author, adj_word)
                        for sim in sim_words:
                            if sim[0] not in synonyms and sim[0] != adj_word:
                                # synonyms.append(sim[0])
                                similar_words.append(sim[0])

                    synonyms.extend([syn.word for syn in adj_object.synonyms.all()
                                     if syn.word not in similar_words and syn.word != adj_word])
                    for sim in similar_words:
                        synonyms.extend([syn.word for syn in Adjective.objects.get(word=sim).synonyms.all()
                                         if syn.word not in similar_words and syn.word != adj_word])
                    syn_gen = SynonymGenerator.load(line, adj, synonyms, similar_words)
                    syn_gen_list.append(syn_gen)

            words = line.split()
            line_split = []
            was_adj = True
            for word in words:
                if word in adj_list:
                    line_split.append(word)
                    was_adj = True
                else:
                    if was_adj:
                        line_split.append(word)
                    else:
                        line_split[-1] += ' ' + word
                    was_adj = False
            original_lines.append(line_split)

        for syn_gen in syn_gen_list:
            if syn_gen.line not in generated_sentences:
                generated_sentences[syn_gen.line] = {}

            generated_sentences[syn_gen.line][syn_gen.adj] = {
                'synonyms': syn_gen.synonyms,
                'similar': syn_gen.w2v_sim,
            }

        os.chdir(f'{root}/adj_suggestion')

    return render(request, 'SuggestAdjectives/suggest.html',
                  {
                      'original': original_lines,
                      'generated': generated_sentences,
                  })


def generated(request):
    original_sentences = []
    generated_sentences = []
    if request.method == 'POST':
        post = request.POST
        sentence_keys = [key for key in post.keys() if 'sentence-' in key]
        for sk in sentence_keys:
            sentence_num = sk.split("-")[-1]
            sentence = post.get(sk)

            for ak in [key for key in post.keys() if f'adj-{sentence_num}' in key]:
                adj_num = ak.split("-")[-1]
                synonym_key = f'synonym-{sentence_num}-{adj_num}'

                sug = post.get(synonym_key)
                adj = post.get(ak)

                sentence = sentence.replace(adj, sug)

            generated_sentences.append(sentence)

    return render(request, 'SuggestAdjectives/generated.html',
                  {
                      'original': original_sentences,
                      'generated': generated_sentences
                  })


def api_check_adjectives_in_db(request):
    words = request.GET.getlist('words[]')
    response = {
        'ok': [],
        'no': [],
    }

    for word in words:
        for p in string.punctuation:
            word.replace(p, '')
        if len(Adjective.objects.filter(word=word)) > 0:
            response['ok'].append(word)
        else:
            response['no'].append(word)

    return HttpResponse(json.dumps(response), content_type='application/json')


def api_save_new_words(request):
    forced = request.GET.getlist('words[]')
    create_synonyms(forced)

    return HttpResponse('')

def get_author_names():
    rel_path = f'{root}/adj_suggestion/SuggestAdjectives/model'
    return [fname for fname in os.listdir(rel_path)
            if os.path.isdir(f'{rel_path}/{fname}') and fname[0] not in ['.', '_']]
