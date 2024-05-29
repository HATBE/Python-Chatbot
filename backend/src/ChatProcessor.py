import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class ChatProcessor:
    def __init__(self):
        self.word2vec = spacy.load('en_core_web_lg')
        self.stopWords = set(stopwords.words('english'))

    def preprocess(self, input_sentence):
        input_sentence = input_sentence.lower()
        input_sentence = re.sub(r'[^\w\s]', '', input_sentence)
        tokens = word_tokenize(input_sentence)
        input_sentence = [i for i in tokens if not i in self.stopWords]
        return input_sentence

    def extractNouns(self, tagged_message):
        message_nouns = [token[0] for token in tagged_message if token[1].startswith("N")]
        return message_nouns

    def computeSimilarity(self, tokens, category):
        output_list = [[token.text, category.text, token.similarity(category)] for token in tokens]
        return output_list
