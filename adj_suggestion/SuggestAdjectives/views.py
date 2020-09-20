from django.shortcuts import render
from .models import Synonyms
import os
import sys
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

        p = os.getcwd()
        os.chdir('C:/Users/Daniel Shin/Desktop/Audrey')

        w2v_model = main.create_model()
        syn_gen_list = []

        for line in lines:
            adj_list = main.parse_input(line)
            for adj in adj_list:
                # TODO: load syn_gen from Model
                syn_gen_list.append(main.find_syn_adj(line, adj, w2v_model))

        for syn_gen in syn_gen_list:
            if syn_gen.line not in generated_sentences:
                generated_sentences[syn_gen.line] = {}

            generated_sentences[syn_gen.line][syn_gen.adj] = syn_gen.generate()

        os.chdir(p)


    return render(request, 'SuggestAdjectives/suggest.html',
                  {
                      'original': original_lines,
                      'suggested': suggested_lines,
                      'generated': generated_sentences,
                  })


def generated(request):
    generated_sentences = []
    if request.method == 'POST':
        target = 1
        while True:
            sentence = request.POST.get(str(target), None)
            if sentence is None:
                break
            generated_sentences.append(sentence)
            target += 1

    return render(request, 'SuggestAdjectives/generated.html',
                  {
                      'generated': generated_sentences
                  })