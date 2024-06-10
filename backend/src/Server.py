import asyncio
import websockets
from .ChatBot import ChatBot
import random
import json

class Server:
    def __init__(self):
        self.chatbot = ChatBot()
        self.connected_clients = set()

    async def handle_client(self, websocket, path):
        # add client
        self.connected_clients.add(websocket)
        print("Client connected. Total connected clients: {}".format(len(self.connected_clients)))

        supporter_name = random.choice(self.chatbot.response_manager.names)

        # send init mesage (currently just with the supporter name)
        await websocket.send(json.dumps({"type": "init", "supporter_name": supporter_name}))
        # send a welcome message to the connected client
        await websocket.send(json.dumps({"type": "message", "text": "Welcome to the Computer support. My name is {}, How can I assist you today?".format(supporter_name)}))

        try:
            async for message in websocket:
                # check if user wants to exit
                if self.chatbot.make_exit(message) or message == "no": # if direct no, then exit too
                    await websocket.send("Ok, Goodby")
                    break

                # generate respoonse
                response = self.chatbot.respond(message)
                
                # send response to user
                await websocket.send(json.dumps({"type": "message", "text": response}))
                await websocket.send(json.dumps({"type": "message", "text": "Do you have any other questions?"}))
        except websockets.ConnectionClosed:
            print("Client disconnected")
        finally:
            # delete client
            self.connected_clients.remove(websocket)
            print("Client disconnected. Total connected clients: {}".format(len(self.connected_clients)))
    
    async def serve(self, port):
        async with websockets.serve(self.handle_client, "localhost", port):
            print("Server started on ws://localhost:{}".format(port))
            await asyncio.Future()  # run forever