from .ChatProcessor import ChatProcessor
from .Response import Response 
from nltk import pos_tag

class ChatBot:
    def __init__(self):
        self.chatProcessor = ChatProcessor()
        self.response_manager = Response()
        # define exit commands that will trigger the bot to end the conversation
        self.exit_commands = ("quit", "goodbye", "exit")

    def make_exit(self, user_message):
        # check if the user message contains any of the exit commands
        for command in self.exit_commands:
            if command in user_message:
                return True
        return False

    def find_entities(self, user_message):
        # preprocess the user message and tag parts of speech
        tagged_user_message = pos_tag(self.chatProcessor.preprocess(user_message))
        message_nouns = self.chatProcessor.extractNouns(tagged_user_message)
        
        # extract nouns from the tagged message
        if not message_nouns:
            return self.response_manager.blank_spot
        
        # convert the extracted nouns and the blank spot response to word vectors
        tokens = self.chatProcessor.word2vec(" ".join(message_nouns))
        category = self.chatProcessor.word2vec(self.response_manager.blank_spot)
        
        # compute the similarity between the tokens and the category
        word2vec_result = self.chatProcessor.computeSimilarity(tokens, category)
        # sort the results based on similarity
        word2vec_result.sort(key=lambda x: x[2])

        # if no results are found, return the blank spot response
        if len(word2vec_result) < 1:
            return self.response_manager.blank_spot
        else:
            # Return the entity with the highest similarity
            return word2vec_result[-1][0]

    def respond(self, user_message):
        # preprocess the user message
        processed_message = self.chatProcessor.preprocess(user_message)
        # Determine the intent of the processed message
        intent = self.response_manager.find_intent(processed_message)

        # if the intent is not a greeting or default, find entities in the message
        entity = self.find_entities(user_message) if intent != "greeting" and intent != "default" else ""
        
        # generate a response based on the intent and the found entity
        response = self.response_manager.get_response(intent, entity)
        
        return response