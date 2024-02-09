import asyncio
import argparse
from controller.event_controller import EventController
import controller.chef_processors
import controller.staff_processors
import controller.management_processors

chef_event_handlers = {
    'OrderPlacedEvent'  : controller.chef_processors.on_order_placed_event,
    # Add more here as needed
}
staff_event_handlers = {
    'OrderPreparedEvent'    : controller.staff_processors.on_order_prepared_event,
    'OrderRecordedEvent'    : controller.staff_processors.on_order_recorded_event,
    'KitchenClosedEvent'    : controller.staff_processors.on_kitchen_closed_event,
    'ShiftChangedEvent'     : controller.staff_processors.on_shift_changed_event,
    # Add more here as needed
}
management_event_handlers = {
    # Add more here as needed
    'OrderPreparedEvent'   : controller.management_processors.on_order_prepared_event,
}

async def run_listener(process, event_handlers):
    controller = EventController('localhost', 6379)
    await controller.start_listening(process, event_handlers)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Run the chef, staff or mgnt controller')
    parser.add_argument('process', choices = ['chef', 'staff', 'mgnt'], help = 'the process to run')
    args = parser.parse_args()

    if args.process == 'chef':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_listener('chef', chef_event_handlers))
        loop.close()

    elif args.process == 'staff':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_listener('staff', staff_event_handlers))
        loop.close()

    elif args.process == 'mgnt':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_listener('mgnt', management_event_handlers))
        loop.close()
