from src.Server import Server
import asyncio

asyncio.run(Server().serve(2000))
