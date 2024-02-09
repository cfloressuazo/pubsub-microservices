import requests
import threading
from controller.event_controller import handle_event

@handle_event('OrderPreparedEvent')
async def on_order_prepared_event(event_data):
    print("-------- Staff Event Processor - OrderPreparedEvent --------")
    print(f"Received OrderPreparedEvent: {event_data}")
    # Send a request to the staff microservice to deliver the order
    threading.Thread(
        target = requests.post,
        args = (
            'http://0.0.0.0:5000/orders/deliver',
        ),
        kwargs = {
            'json': event_data,
        }
    ).start()

@handle_event('OrderRecordedEvent')
async def on_order_recorded_event(event_data):
    print("-------- Staff Event Processor - OrderRecordedEvent --------")
    print(f"Received OrderRecordedEvent: {event_data}")
    # Send a request to the staff microservice to deliver the order

@handle_event('KitchenClosedEvent')
async def on_kitchen_closed_event(event_data):
    print("-------- Staff Event Processor - KitchenClosedEvent --------")
    print(f"Received KitchenClosedEvent: {event_data}")
    # Send a request to the staff microservice clear the data and cache
    threading.Thread(
        target = requests.post,
        args = (
            'http://0.0.0.0:5000/menu/orders-served/clear-cache',
        )
    ).start()

@handle_event('ShiftChangedEvent')
async def on_shift_changed_event(event_data):
    print("-------- Staff Event Processor - ShiftChangedEvent --------")
    print(f"Received ShiftChangedEvent: {event_data}")
    # Send a request to the staff microservice clear the cached view
    threading.Thread(
        target = requests.post,
        args = (
            'http://0.0.0.0:5000/orders/deliver',
        ),
        kwargs = {
            'json': event_data,
        }
    ).start()
