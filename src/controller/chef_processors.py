import aiohttp
import requests
import threading
from controller.event_controller import handle_event

@handle_event('OrderPlacedEvent')
async def on_order_placed_event(event_data):
    print("-------- Chef Event Processor - OrderPlacedEvent --------")
    print(f"Received OrderPlacedEvent: {event_data}")
    # Send a request to the Chefs microservice to prepare the order
    # async with aiohttp.ClientSession() as session:
    #     async with session.post('http://0.0.0.0:5001/orders/prepare', json = event_data) as resp:
    #         print(resp.status)
    #         print(await resp.text())
    threading.Thread(
        target = requests.post,
        args = (
            'http://0.0.0.0:5001/orders/prepare',
        ),
        kwargs = {
            'json': event_data,
        }
    ).start()

