import asyncio
import requests
import threading
from controller.event_controller import handle_event

def send_post_request(url, json):
    response = requests.post(url, json = json)
    return True

@handle_event('OrderPreparedEvent')
async def on_order_prepared_event(event_data):
    print("-------- Management Event Processor - OrderPreparedEvent --------")
    print(f"Received OrderPreparedEvent: {event_data}")
    # loop = asyncio.get_event_loop()
    # loop.run_in_executor(
    #     None, # TODO: add missing executor
    #     send_post_request,
    #     'http://0.0.0.0:5002/orders/record',
    #     event_data,
    # )
    threading.Thread(
        target = requests.post,
        args = (
            'http://0.0.0.0:5002/orders/record',
        ),
        kwargs = {
            'json': event_data,
        }
    ).start()
    print("-------- Management Event Processor - OrderPreparedEvent --------")
    print(f"Sent OrderPreparedEvent: {event_data}")

    # Send a request to the staff microservice to deliver the order
