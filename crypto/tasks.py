import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
import asyncio
import json

@shared_task(bind=True)
def test_func(self):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    loop.run_until_complete(channel_layer.group_send("data_update", {
        'type': 'update_data',
        'text': data,
    }))
    return "completed"