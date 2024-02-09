import json
import uuid
from datetime import datetime
from flask import Blueprint, jsonify, request
from management.app import redis_client

mgnt_bp = Blueprint('management', __name__)

@mgnt_bp.route('/orders/record', methods = ['POST'])
def record_order():
    # Handle RecordOrderCommand
    data = request.get_json()
    event_data = data['event_data']
    # Record total number of orders served for each dish in the database
    # ...
    # Pull from redis the orders_served dictionary
    orders_served = redis_client.get('orders_served')

    if not orders_served:
        orders_served = {}
    else:
        orders_served = json.loads(orders_served)

    for dish in event_data['dish_details']:
        if dish not in orders_served:
            orders_served[dish] = 0

        orders_served[dish] += 1

    # Update redis with the new orders_served dictionary
    redis_client.set('orders_served', json.dumps(orders_served))

    print(f'Orders served: {orders_served}')

    # Publish OrderRecordedEvent to message broker
    event = {
        'event_id'      : str(uuid.uuid4()),
        'event_type'    : 'OrderRecordedEvent',
        'event_source'  : 'management',
        'timestamp'     : str(datetime.utcnow()),
        'event_data'    : {
            'order_status': 'recorded',
            'message': 'update-available-dishes',
        },
    }
    redis_client.publish('management.events', json.dumps(event))

    return jsonify({'message': 'Order recorded'}), 200

@mgnt_bp.route('/kitchen/close', methods = ['POST'])
def close_kitchen():
    # Handle CloseKitchenCommand
    # Delete the key orders_served from redis
    redis_client.delete('orders_served')

    # Publish KitchenClosedEvent to message broker
    event = {
        'event_id'      : str(uuid.uuid4()),
        'event_type'    : 'KitchenClosedEvent',
        'event_source'  : 'management',
        'timestamp'     : str(datetime.utcnow()),
        'event_data'    : {
            'message': 'kitchen-closed',
        },
    }
    redis_client.publish('management.events', json.dumps(event))

    print("Kitchen closed!!!!!!!")

    return jsonify({'message': 'Kitchen closed'}), 200

@mgnt_bp.route('/ingredients/buy', methods = ['POST'])
def buy_ingredients():
    # Handle BuyIngredientsCommand
    data = request.get_json()
    # The buy ingredients command simulates the data ingestion process,
    # This process sends an event about the ingredients that were bought
    # to the message broker
    # The waiters should update the menu with the new ingredients
    ...


@mgnt_bp.route('/prices/update', methods = ['POST'])
def update_prices():
    # Handle UpdatePricesCommand
    # The update prices command simulates a process that updates the prices
    # of the dishes on the menu
    data = request.get_json()
    ...
