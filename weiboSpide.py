import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from config import *

def get_page(since_id):
    #获取微博json数据
    params = {
        'type': 'uid',
        'value': USER_ID,
        'containerid': CONTAINER_ID,
    }
    if since_id!= 0:
        params['since_id'] = since_id
    url = BASE_URL + urlencode(params)
    try:
        response = requests.get(url,headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"HTTPError: {e}")
    except requests.ConnectionError as e:
        print(f"ConnectionError: {e}")
    except requests.Timeout as e:
        print(f"Timeout: {e}")
    except requests.RequestException as e:
        print(f"RequestException: {e}")
    return None

def parse_page(json):
    #解析JSON，提取微博数据
    if json and 'data' in json and 'cards' in json['data']:
        items = json['data']['cards']
        for item in items:
            mblog = item.get('mblog')
            if mblog:
                weibo = {
                    'id' : mblog.get('id'),
                    'text': pq(mblog.get('text')).text(),
                    'attitudes': mblog.get('attitudes_count'),
                    'comments': mblog.get('comments_count'),
                    'reposts': mblog.get('reposts_count')
                }
                yield weibo