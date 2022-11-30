from positive_score import pos_score
from negative_score import neg_score
from polarity_score import polar_score
from subjectivity_score import subject_score
from avg_sent_len import avg_sent_len
from percentage_of_complex_words import per_of_comp_words
from Fog_index_calculator import fog_index
from Average_words_per_sentence import avg_words_per_sentence
from Complex_word_count import comp_word_count
from Word_counter import word_count
from Syllable_word_counter import syy_per_word
from Personal_pronoun_tag import per_pronoun
from Average_word_Length import avg_word_length
import trafilatura
import pandas as pd

df_Output = pd.DataFrame(
    columns=['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
             'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE',
             'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'])


df = pd.DataFrame(pd.read_excel("Input.xlsx"))
features = []
urls = df['URL'].tolist()
for x in range(len(urls)):
    try:
        downloaded = trafilatura.fetch_url(urls[x])
        data = trafilatura.extract(downloaded)
        features.append(pos_score(data))  # 1  pos
        features.append(neg_score(data))  # 2  neg
        features.append(polar_score(data))  # 3 polarity
        features.append(subject_score(data))  # 4 subjectivity
        features.append(avg_sent_len(data))  # 5 average sentence length
        features.append(per_of_comp_words(data))  # 6 percentage of complex words
        features.append(fog_index(data))  # 7 calculate fog index
        features.append(avg_words_per_sentence(data))  # 8 cal avg number of words per sentence
        features.append(comp_word_count(data))  # 9 Complex word count
        features.append(word_count(data))  # 10-word count
        features.append(syy_per_word(data))  # 11- syllable per word
        features.append(per_pronoun(data))  # 12 - personal prononun
        features.append(avg_word_length(data))  # 13 - avg words length
        df_Output.loc[len(df_Output)] = features
        features.clear()

    except:
        continue
print(features)
Output = pd.concat([df, df_Output], axis=1, join='inner')
Output.to_excel("Output.xlsx")

