import asyncio
import websockets
from .ChatBot import ChatBot
import random

class Server:
    def __init__(self):
        self.chatbot = ChatBot()
        self.connected_clients = set()

    async def handle_client(self, websocket, path):
        # Register client
        self.connected_clients.add(websocket)
        print(f"Client connected. Total connected clients: {len(self.connected_clients)}")

        # Send a welcome message to the connected client
        await websocket.send("Welcome to computer support. My name is {}, How can I assist you today?".format(random.choice(self.chatbot.response_manager.names)))

        try:
            async for message in websocket:
                #print(f"Received message: {message}")
                
                if self.chatbot.make_exit(message):
                    await websocket.send("Goodby")
                    break

                response = self.chatbot.respond(message)
                
                await websocket.send(response)
                await websocket.send("Do you have any other questions?")
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