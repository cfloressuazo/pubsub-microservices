import json
import asyncio
import uuid
from datetime import datetime
from flask import Blueprint, jsonify, request, current_app
from chef.app import redis_client


chef_bp = Blueprint('chef', __name__)

@chef_bp.route('/orders/prepare', methods = ['POST'])
async def prepare_order():
    print(request.get_json())
    try:
        # Handle PrepareOrderCommand
        data = request.get_json()
        event_data = data['event_data']

        order_id = event_data['order_id']
        dish_details = event_data['dish_details']
        event = {
            'event_id'      : str(uuid.uuid4()),
            'event_type'    : 'OrderPreparingEvent',
            'event_source'  : 'chef',
            'timestamp'     : str(datetime.utcnow()),
            'event_data'    : {
                'order_id'      : order_id,
                'dish_details'  : dish_details,
                'order_status'  : 'preparing',
            },
        }

        # Load event data into database
        # ...
        # Publish OrderPreparingEvent to message broker
        redis_client.publish('chef.events', json.dumps(event))

        # Simulate cooking time (long running task in the background)
        await cook_order(order_data = event['event_data'])

        return jsonify({'order_id': order_id}), 200

    except Exception as e:
        print('Error in prepare_order()', e)
        event = {
            'event_id'      : str(uuid.uuid4()),
            'event_type'    : 'OrderPreparingFailedEvent',
            'event_source'  : 'chef',
            'timestamp'     : str(datetime.utcnow()),
            'error'         : str(e),
            'event_data'    : {
                'order_id'      : order_id,
                'dish_details'  : dish_details,
                'order_status'  : 'preparing_failed',
            },
        }
        redis_client.publish('chef.events', json.dumps(event))

        return jsonify({'error': 'Internal server error'}), 500

# Simulate cooking time
async def cook_order(order_data):
    for dish in order_data['dish_details']:
        print(f'Cooking {dish} for 1 minutes')
        current_app.logger.info(f'Cooking {dish} for 1 minutes')
        await asyncio.sleep(4)

    event = {
        'event_id'      : str(uuid.uuid4()),
        'event_type'    : 'OrderPreparedEvent',
        'event_source'  : 'chef',
        'timestamp'     : str(datetime.utcnow()),
        'event_data'    : {
            'order_id'  : order_data['order_id'],
            'dish_details'  : order_data['dish_details'],
            'order_status'  : 'prepared',
        }
    }

    # Load event data into database
    # ...

    # Submit OrderPreparedEvent to message broker
    redis_client.publish('chef.events', json.dumps(event))

    return True
