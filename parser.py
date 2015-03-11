#codding: utf-8

import feedparser
import requests
import json


FACEBOOK_GRAPH_ENDPOINT = ''
FACEBOOK_RSS_ENDPOINT = ''

def get_page_id(fanpage_url):
	graph_url = '%s%s' % (FACEBOOK_GRAPH_ENDPOINT, fanpage_url)