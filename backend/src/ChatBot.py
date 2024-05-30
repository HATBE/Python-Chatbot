from .ChatProcessor import ChatProcessor
from .Response import Response 
from nltk import pos_tag

class ChatBot:
    def __init__(self):
        self.chatProcessor = ChatProcessor()
        self.response_manager = Response()
        self.exit_commands = ("quit", "goodbye", "exit")

    def make_exit(self, user_message):
        for command in self.exit_commands:
            if command in user_message:
                return True
        return False

    def find_entities(self, user_message):
        tagged_user_message = pos_tag(self.chatProcessor.preprocess(user_message))
        message_nouns = self.chatProcessor.extractNouns(tagged_user_message)
        if not message_nouns:
            return self.response_manager.blank_spot
        tokens = self.chatProcessor.word2vec(" ".join(message_nouns))
        category = self.chatProcessor.word2vec(self.response_manager.blank_spot)
        word2vec_result = self.chatProcessor.computeSimilarity(tokens, category)
        word2vec_result.sort(key=lambda x: x[2])
        if len(word2vec_result) < 1:
            return self.response_manager.blank_spot
        else:
            return word2vec_result[-1][0]

    def respond(self, user_message):
        processed_message = self.chatProcessor.preprocess(user_message)
        intent = self.response_manager.find_intent(processed_message)
        entity = self.find_entities(user_message) if intent != "greeting" and intent != "default" else ""
        response = self.response_manager.get_response(intent, entity)
        return response