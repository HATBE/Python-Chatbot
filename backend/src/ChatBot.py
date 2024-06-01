from .ChatProcessor import ChatProcessor
from .ResponseManager import ResponseManager 

class ChatBot:
    def __init__(self):
        self.chatProcessor = ChatProcessor(self)
        self.response_manager = ResponseManager()
        # define exit commands that will trigger the bot to end the conversation
        self.exit_commands = ("quit", "goodbye", "exit")

    def make_exit(self, user_message):
        # check if the user message contains any of the exit commands
        for command in self.exit_commands:
            if command in user_message:
                return True
        return False

    def respond(self, user_message):
        # preprocess the user message
        processed_message = self.chatProcessor.preprocess(user_message)
        # Determine the intent of the processed message
        intent = self.response_manager.find_intent(processed_message)

        # if the intent is not a greeting or default, find entities in the message
        entity = self.chatProcessor.find_entities(user_message) if intent != "greeting" and intent != "default" else ""
        
        # generate a response based on the intent and the found entity
        response = self.response_manager.get_response(intent, entity)
        
        return response