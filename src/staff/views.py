import json
import uuid
from datetime import datetime
from flask import Blueprint, jsonify, request

from staff.app import redis_client, cache

staff_bp = Blueprint('staff', __name__)

#################################################
# Read views
#################################################
@staff_bp.route('/menu', methods = ['GET'])
@cache.cached(timeout = 60)
def show_menu():
    # Query the database for available items
    available_items = ['item1', 'item2', 'item3']

    # Query the database for unavailable items
    unavailable_items = ['item4', 'item5']

    menu = {
        'available_items': available_items,
        'unavailable_items': unavailable_items
    }

    return jsonify(menu), 200

@staff_bp.route('/menu/orders-served', methods = ['GET'])
@cache.cached(timeout = 60)
def show_orders_served():
    # Get orders served from Redis
    orders_served = redis_client.get('orders_served')
    if orders_served:
        orders_served = json.loads(orders_served)
    else:
        orders_served = {}

    return jsonify(orders_served), 200

#################################################
# Write & Execution views
#################################################
@staff_bp.route('/orders', methods = ['POST'])
def take_order():
    # Handle TakeOrderCommand
    data = request.get_json()
    if 'table_number' in data and 'dishes' in data:
        order_id = str(uuid.uuid4())
        table_number = data['table_number']
        dishes = data['dishes']
        event = {
            'event_id'      : str(uuid.uuid4()),
            'event_type'    : 'OrderPlacedEvent',
            'event_source'  : 'staff',
            'timestamp'     : str(datetime.utcnow()),
            'event_data'    : {
                'order_id'      : order_id,
                'table_number'  : table_number,
                'dish_details'  : dishes,
                'order_status'  : 'placed',
            },
        }
        # Publish OrderPlacedEvent to message broker
        redis_client.publish('staff.events', json.dumps(event))
        print(f'Order placed: {event}')

        return jsonify({'order_id': order_id}), 200
    else:
        print('Order not placed')
        return jsonify({'error': 'Invalid request'}), 400

@staff_bp.route('/orders/deliver', methods = ['POST'])
def deliver_order():
    # Handle MarkOrderAsDeliveredCommand
    data = request.get_json()
    event_data = data['event_data']
    if 'order_id' in event_data:
        order_id = event_data['order_id']
        # pull table_number from database via order_id
        table_number = '1'

        dishes = event_data['dish_details']
        event = {
            'event_type'    : 'OrderDeliveredEvent',
            'event_source'  : 'staff',
            'timestamp'     : str(datetime.utcnow()),
            'event_data'    : {
                'order_id'      : order_id,
                'table_number'  : table_number,
                'dish_details'  : dishes,
                'order_status'  : 'delivered',
            },
        }

        # Load event data into database
        # ...
        # Publish OrderDeliveredEvent to message broker
        redis_client.publish('staff.events', json.dumps(event))
        print(f'Order delivered: {event}')

        return jsonify({'order_id': order_id}), 200
    else:
        print('Order not delivered')
        return jsonify({'error': 'Invalid request'}), 400

#################################################
# Cache Operations
#################################################
@staff_bp.route('/menu/orders-served/clear-cache', methods = ['POST'])
def clear_orders_served_cache():
    cache.delete_memoized(show_orders_served)
    print('Cache cleared successfully')
    return jsonify({'message': 'Cache cleared successfully'}), 200
