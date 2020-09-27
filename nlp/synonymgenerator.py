from crawler.crawl_main import get_synonyms, get_antonyms


class SynonymGenerator:
    def __init__(self, line, adj):
        self.line = line
        self.adj = adj
        self.synonyms = []
        
    def create(self, w2v_model):
        if self.adj in w2v_model.get_vocabs():
            similar = w2v_model.most_similar(self.adj)
            synonyms = get_synonyms(self.adj)
            antonyms = get_antonyms(self.adj)

            idx = 0
            count = 0
            while idx < len(similar):
                sim = similar[idx][0]

                dist = 0
                dist_cnt = 0
                for ant in antonyms:
                    if ant in w2v_model.get_vocabs():
                        dist += w2v_model.similarity(ant, sim)
                        dist_cnt += 1

                if dist_cnt != 0:
                    dist = dist / dist_cnt

                if sim not in antonyms and (dist_cnt == 0 or dist < 0.2):
                    synonyms.extend(get_synonyms(sim))
                    count += 1

                if count == 5:
                    break

                idx += 1

            self.synonyms = synonyms

    def generate(self):
        results = []
        for syn in self.synonyms:
            new_line = self.line.replace(self.adj, syn)
            words = new_line.split()
            for i, word in enumerate(words):
                if word[0] in ['a', 'e', 'i', 'o', 'u'] and i > 0 and words[i - 1] == 'a':
                    words[i - 1] = 'an'
                elif word[0] not in ['a', 'e', 'i', 'o', 'u'] and i > 0 and words[i - 1] == 'an':
                    words[i - 1] = 'a'

            results.append(' '.join(words))

        return results

    @staticmethod
    def load(line, adj, synonyms):
        syn_gen = SynonymGenerator(line, adj)
        syn_gen.synonyms = synonyms

        return syn_gen

