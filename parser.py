# codding: utf-8

import feedparser
import requests
import json


FACEBOOK_GRAPH_ENDPOINT = 'https://graph.facebook.com/'
FACEBOOK_RSS_ENDPOINT = 'https://www.facebook.com/feeds/page.php?format=rss20&id='


def get_graph_data(fanpage_name):
    graph_url = '%s%s' % (FACEBOOK_GRAPH_ENDPOINT, fanpage_name)
    page_meta = requests.get(graph_url)
    page_meta.raise_for_status()
    return json.loads(page_meta.text)


def get_last_entry(fanpage_id):
    feed = feedparser.parse('%s%s' % (FACEBOOK_RSS_ENDPOINT, fanpage_id))
    return feed['entries'][0]['summary']


def get_last_entry_for_fanpage_name(fanpage_name):
    page_id = get_graph_data(fanpage_name)['id']
    return get_last_entry(page_id)


def fetch_restaurants_data(names_list):
    restaurants_data = {}
    for restaurant_name in names_list:
        graph_data = get_graph_data(restaurant_name)
        full_name = graph_data['name']
        restaurants_data[full_name] = {
            'id': graph_data['id'],
            'url': graph_data['link']
        }
    json_dump = json.dumps(restaurants_data, indent=4)
    db = open('restaurants.json', 'wb')
    db.write(json_dump)
    db.close()
