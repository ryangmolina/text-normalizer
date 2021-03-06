import os
from pprint import pprint
from nltk.tokenize import word_tokenize
try:
    from .training.data.textnormalizer import TextNormalizer
    from .training.data.spellcorrector import SpellCorrector
    from .training.data.textnoisifier import TextNoisifier
    from .utils.helper import csv_to_dict
except SystemError:
    from training.data.textnormalizer import TextNormalizer
    from training.data.textnoisifier import TextNoisifier
    from training.data.spellcorrector import SpellCorrector
    from utils.helper import csv_to_dict

FILE_PATH = os.path.dirname(__file__)

accent_words_dict = csv_to_dict(
    os.path.join(FILE_PATH, 'training', 'data','accented_words.dic'))

with open(os.path.join(FILE_PATH, 'training', 'data', 'pandiwa.dic'), \
        'r') as pandiwa_file:
    pandiwa_words_dict = pandiwa_file.read().splitlines()
    

phonetic_subwords_dict = csv_to_dict(
    os.path.join(FILE_PATH, 'training', 'data', 'phonetically_styled_subwords.dic'))

phonetic_words_dict = csv_to_dict(
    os.path.join(FILE_PATH, 'training', 'data', 'phonetically_styled_words.dic'))

pprint(accent_words_dict)
dict_path = os.path.join(FILE_PATH, 'training', 'data', 'corpus', 'tagalog_sent.txt')

with open(os.path.join(FILE_PATH, 'training', 'data', 'hyph_fil.tex'), 'r') as f:
    hyphenator_dict = f.read()


accent_words_dict = {v2: k 
                     for k, v in accent_words_dict.items()
                     for v2 in v}
spell_corrector = SpellCorrector(dict_path=dict_path)
tn = TextNormalizer(accent_words_dict=accent_words_dict,
                    hyphenator_dict=hyphenator_dict,
                    pandiwa_words_dict=pandiwa_words_dict,
                    spell_corrector=spell_corrector)

# tn = TextNoisifier(accent_words_dict=accent_words_dict,
#                     phonetic_words_dict=phonetic_words_dict,
#                     phonetic_subwords_dict=phonetic_subwords_dict,
#                     hyphenator_dict=hyphenator_dict)
# while True:
#     word = input(">>> ")
#     print(' '.join([tn.phonetic_style(mwe) for mwe in tn.mwe_tokenizer.tokenize(word.split())]))

with open(os.path.join(FILE_PATH, 'training', 'data', 'corpus', 'merged_bicol.txt'), 'r') as in_fp:
    lines = in_fp.read().splitlines()
    with open(os.path.join(FILE_PATH, 'training', 'data', 'corpus', 'merged_bicol_v2.txt'), 'w') as out_fp:
        for line in lines:
            # tokens = line.split()
            tokens = word_tokenize(line)
            # tokens = tn.mwe_tokenizer.tokenize(tokens)
            # line = ' '.join([tn.accent_style(mwe) for mwe in tokens])
            # print(line, file=out_fp)
            print(' '.join(tokens), file=out_fp)
