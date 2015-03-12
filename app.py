# coding: utf-8
from __future__ import unicode_literals

import datetime
import json
import os
import redis

from flask import Flask
from flask import render_template

from parser import get_last_entry

app = Flask(__name__)
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)
CACHE_TIME = datetime.timedelta(hours=1)


@app.route('/')
def index():
    last_entries = []
    restaurants = json.loads(open('restaurants.json').read())
    for restaurant_name in restaurants:
        place_data = restaurants[restaurant_name]
        place_id = place_data['id']
        cache_key = 'last-entry-%s' % (place_id,)
        last_entry = redis.get(cache_key)
        if last_entry:
            last_entry = last_entry.decode('utf-8')
        else:
            last_entry = get_last_entry(place_id)
            redis.setex(name=cache_key, time=CACHE_TIME, value=last_entry)
        
        last_entries.append(
            {'name': restaurant_name, 'url': place_data['url'],
             'last_entry': last_entry}
        )
    return render_template('index.html', last_entries=last_entries)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    app.run(debug=debug, port=port, host='0.0.0.0')
