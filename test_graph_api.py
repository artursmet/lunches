from __future__ import unicode_literals
import os

from graph import Graph


class Facebook(object):
    GRAPH_API = 'https://graph.facebook.com'
    proxy = None
    oauth2_token = os.environ('FACEBOOK_APP_TOKEN', None)


def get_post_and_picture(fanpage_name):
    posts_endpoint = '%s/posts/' % fanpage_name
    graph = Graph(facebook=Facebook(), path=posts_endpoint)
    posts_data = graph.get()['data']
    last_post = posts_data[0]
    if 'picture' in last_post:
        last_post_id = last_post['object_id']
        graph = Graph(Facebook(), path=last_post_id)
        post_data = graph.get()
        image = post_data['images'][0]['source']
    else:
        image = None

    return {
        'page_id': last_post['from']['id'],
        'message': last_post['message'],
        'image': image if image else '',
        'created': last_post['created_time']
    }
