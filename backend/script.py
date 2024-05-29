import re
import spacy
import socket
from nltk.corpus import stopwords
from collections import Counter
from nltk import pos_tag
from nltk.tokenize import word_tokenize

class Response:
    def __init__(self):
        self.responses = {
            "restart": "Have you tried restarting your {}? It often resolves many issues.",
            "slow": "To fix a slow {} performance, try closing unnecessary applications.",
            "overheat": "If your {} is overheating, ensure it's placed in a well-ventilated area and clean any dust from the vents.",
            "greeting": "I'm doing well, thank you! How can I assist you with your computer problem?",
            "wifi": "If you're having Wi-Fi issues with your {}, try restarting your router or checking your network settings.",
            "battery": "If your {} battery is draining quickly, try reducing screen brightness and closing unused applications.",
            "software": "To resolve software issues on your {}, try reinstalling the problematic application.",
            "update": "Ensure your {} has the latest updates installed. Sometimes updates fix many issues.",
            "virus": "If you suspect a virus on your {}, run a full system antivirus scan.",
            "password": "If you've forgotten your {} password, you can reset it using the 'Forgot Password' option on the login screen.",
            "backup": "It's important to regularly backup your {} data to prevent data loss.",
            "hardware": "If you're experiencing hardware issues with your {}, check for any loose cables or connections.",
            "screen": "If your {} screen is flickering or not displaying properly, try adjusting the display settings.",
            "keyboard": "If your {} keyboard isn't working, try reconnecting it or checking for driver updates.",
            "sound": "If you're having sound issues on your {}, ensure the audio drivers are up to date and check the volume settings.",
            "default": "I did not understand that. Can you please describe your problem in more detail?"
        }
        self.keywords = {
            "restart": ["restart", "reboot", "boot"],
            "slow": ["slow", "lag", "performance"],
            "overheat": ["overheat", "hot", "heat"],
            "greeting": ["hello", "hi", "how are you"],
            "wifi": ["wifi", "wireless network", "internet", "network"],
            "battery": ["battery", "battery draining", "charge", "charging"],
            "software": ["software", "application", "app", "program"],
            "update": ["update", "upgrade", "patch"],
            "virus": ["virus", "malware", "spyware", "antivirus"],
            "password": ["password", "login", "signin"],
            "backup": ["backup", "save", "restore"],
            "hardware": ["hardware", "device", "component"],
            "screen": ["screen", "display", "monitor"],
            "keyboard": ["keyboard", "keys", "typing"],
            "sound": ["sound", "audio", "volume", "speaker"]
        }
        self.blank_spot = "computer"

    def get_response(self, key, entity=None):
        if key not in self.responses:
            return self.responses["default"]
        return self.responses[key].format(entity)

    def find_intent(self, processed_message):
        processed_message = " ".join(processed_message)  # Convert list to string for phrase matching

        for intent,words in self.keywords.items():
            for word in words:
                if word in processed_message:
                    return intent
        return "default"

class ChatBot:
    def __init__(self):
        self.chatProcessor = ChatProcessor()
        self.response_manager = Response()
        self.exit_commands = ("quit", "goodbye", "exit", "no")

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

class Server:
    def __init__(self):
        self.chatbot = ChatBot()
    
    def serve(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            try:
                server_socket.bind(("127.0.0.1", port))
                server_socket.listen()
                print(f'Server started and listening on port {port}')

                while True:
                    client_socket, client_address = server_socket.accept()
                    print(f'Accepted connection from {client_address}')

                    with client_socket:
                        client_socket.sendall(("Welcome to computer support. How can I assist you today?" + '\n').encode('utf-8'))
                        buffer = ""
                        while True:
                            data = client_socket.recv(1024).decode('utf-8')
                            if not data:
                                print('No data received. Closing connection.')
                                break

                            buffer += data

                            if '\n' in buffer:
                                message, buffer = buffer.split('\n', 1)
                                
                                if self.chatbot.make_exit(message):
                                    client_socket.sendall(("Good Bye" + '\n').encode('utf-8'))
                                    break

                                response = self.chatbot.respond(message)
                                client_socket.sendall((response + '\n').encode('utf-8'))
                                client_socket.sendall(("Do you have any other questions?" + '\n').encode('utf-8'))
            except Exception as e:
                print(f"An error occurred: {e}")


Server().serve(2000)
