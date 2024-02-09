import asyncio
import json
from typing import Dict
import redis
from functools import wraps

def handle_event(event_type):
    def decorator(func):
        @wraps(func)
        def wrapper(event_data):
            if event_data.get('event_type') == event_type:
                # print(f"Received {event_type}: {event_data}")
                return func(event_data)
        return wrapper
    return decorator

class EventController:
    def __init__(self, redis_host, redis_port):
        self.redis_client = redis.Redis(
            host = redis_host, port = redis_port)
        self.pubsub = self.redis_client.pubsub()

        self.channels_to_subscribe = [
            'chef.events',
            'staff.events',
            'management.events'
        ]
        for channel in self.channels_to_subscribe:
            self.pubsub.subscribe(channel)

    async def start_listening(self, process: str, event_handlers: Dict[str, callable]):
        print(f"Event Controller for {process} - Start Listening")
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                event_data = message['data']
                await self.process_event(event_handlers, event_data)

    async def process_event(self, event_handlers: Dict[str, callable], event_data: str):
        # Dispatch the event to the appropriate event handler based on event type
        event_data = json.loads(event_data)
        event_type = event_data.get('event_type')
        if event_type in event_handlers:
            await event_handlers[event_type](event_data)
