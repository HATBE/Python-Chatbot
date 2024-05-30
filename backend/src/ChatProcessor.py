import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class ChatProcessor:
    def __init__(self):
        # load the large English model for word vectors and NLP tasks
        self.word2vec = spacy.load('en_core_web_lg')
        # load the set of stopwords in English
        self.stopWords = set(stopwords.words('english'))

    def preprocess(self, input_sentence):
        # convert the input sentence to lowercase
        input_sentence = input_sentence.lower()
        # remove punctuation from the input sentence
        input_sentence = re.sub(r'[^\w\s]', '', input_sentence)
        # tokenize the sentence into words
        tokens = word_tokenize(input_sentence)
        # remove stopwords from the tokenized words
        input_sentence = [i for i in tokens if not i in self.stopWords]
        return input_sentence

    def extractNouns(self, tagged_message):
        # extract nouns from the tagged message (words tagged with parts of speech)
        message_nouns = [token[0] for token in tagged_message if token[1].startswith("N")]
        return message_nouns

    def computeSimilarity(self, tokens, category):
        # compute the similarity between each token and the category word
        output_list = [[token.text, category.text, token.similarity(category)] for token in tokens]
        return output_list
