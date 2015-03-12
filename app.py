# coding: utf-8
import json
from flask import Flask
from flask import render_template
from parser import get_last_entry

app = Flask(__name__)


@app.route('/')
def index():
    last_entries = []
    restaurants = json.loads(open('restaurants.json').read())
    for restaurant_name in restaurants:
        place_data = restaurants[restaurant_name]
        last_entries.append(
            {'name': restaurant_name, 'url': place_data['url'],
             'last_entry': get_last_entry(place_data['id'])}
        )
    return render_template('index.html', last_entries=last_entries)


if __name__ == '__main__':
    app.run(debug=True)