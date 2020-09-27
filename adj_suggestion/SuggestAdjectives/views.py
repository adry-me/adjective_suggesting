from django.shortcuts import render
from .models import Adjective
from .create_dictionary import save
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


# Create your views here.
def sample(request):
    return render(request, 'SuggestAdjectives/sample.html')


def input_contents(request):
    return render(request, 'SuggestAdjectives/input_contents.html')


def suggest(request):
    original_lines = []
    suggested_lines = []
    generated_sentences = {}
    if request.method == 'POST':
        input_text_raw = request.POST.get('input-text', '')
        lines = list(map(str.rstrip, input_text_raw.split('\n')))

        os.chdir(root)

        w2v_model = main.create_model()
        syn_gen_list = []

        for line in lines:
            adj_list = []

            for word in line.split():
                if len(Adjective.objects.filter(word=word)) > 0:
                    adj_list.append(word)
            for adj in adj_list:
                adj_objects = Adjective.objects.filter(word=adj)
                # if len(adj_objects) == 0:
                #     syn_gen = main.find_syn_adj(line, adj, w2v_model)
                #     syn_gen_list.append(syn_gen)
                #     adj_object = Adjective(word=adj)
                #     adj_object.save()
                #     syn_objects = save(syn_gen.synonyms)
                #     for syn_obj in syn_objects:
                #         adj_object.synonyms.add(syn_obj)
                # else:
                adj_object = adj_objects[0]
                synonyms = [syn.word for syn in adj_object.synonyms.all()]
                syn_gen = SynonymGenerator.load(line, adj, synonyms)
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

            generated_sentences[syn_gen.line][syn_gen.adj] = syn_gen.synonyms

        os.chdir(root)


    return render(request, 'SuggestAdjectives/suggest.html',
                  {
                      'original': original_lines,
                      'suggested': suggested_lines,
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
            print(sentence)

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