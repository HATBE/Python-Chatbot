import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

class ChatProcessor:
    def __init__(self, chatbot):
        # load the large English model for word vectors and NLP tasks
        self.word2vec = spacy.load('en_core_web_lg')
        # load the set of stopwords in English
        self.stopWords = set(stopwords.words('english'))

        self.chatbot = chatbot

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

    def find_entities(self, user_message):
        # preprocess the user message and tag parts of speech
        tagged_user_message = pos_tag(self.preprocess(user_message))
        message_nouns = self.extractNouns(tagged_user_message)
        
        # extract nouns from the tagged message
        if not message_nouns:
            return self.chatbot.response_manager.blank_spot
        
        # convert the extracted nouns and the blank spot response to word vectors
        tokens = self.word2vec(" ".join(message_nouns))
        category = self.word2vec(self.chatbot.response_manager.blank_spot)
        
        # compute the similarity between the tokens and the category
        word2vec_result = self.computeSimilarity(tokens, category)
        # sort the results based on similarity
        word2vec_result.sort(key=lambda x: x[2])

        # if no results are found, return the blank spot response
        if len(word2vec_result) < 1:
            return self.chatbot.response_manager.blank_spot
        else:
            # Return the entity with the highest similarity
            return word2vec_result[-1][0]