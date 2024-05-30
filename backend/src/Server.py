import asyncio
import websockets
from .ChatBot import ChatBot
import random
import json

# TODO: first message is information like supporter name, in frontend show the supporter name on top of the message

class Server:
    def __init__(self):
        self.chatbot = ChatBot()
        self.connected_clients = set()

    async def handle_client(self, websocket, path):
        # Register client
        self.connected_clients.add(websocket)
        print(f"Client connected. Total connected clients: {len(self.connected_clients)}")

        supporter_name = random.choice(self.chatbot.response_manager.names)

        await websocket.send(json.dumps({"type": "init", "supporter_name": supporter_name}))
        # Send a welcome message to the connected client
        await websocket.send(json.dumps({"type": "message", "text": "Welcome to the Computer support. My name is {}, How can I assist you today?".format(supporter_name)}))

        try:
            async for message in websocket:    
                if self.chatbot.make_exit(message):
                    await websocket.send("Ok, Goodby")
                    break

                response = self.chatbot.respond(message)
                
                await websocket.send(json.dumps({"type": "message", "text": response}))
                await websocket.send(json.dumps({"type": "message", "text": "Do you have any other questions?"}))
        except websockets.ConnectionClosed:
            print("Client disconnected")
        finally:
            # Unregister client
            self.connected_clients.remove(websocket)
            print(f"Client disconnected. Total connected clients: {len(self.connected_clients)}")
    
    async def serve(self, port):
        async with websockets.serve(self.handle_client, "localhost", port):
            print("Server started on ws://localhost:{}".format(port))
            await asyncio.Future()  # Run forever