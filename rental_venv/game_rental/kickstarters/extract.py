import requests
import json
from bs4 import BeautifulSoup

def get_kickstarter_html(category_id, sort_criteria, page_num):
    response = requests.get('https://www.kickstarter.com/discover/advanced?category_id=%s&sort=%s&seed=2528650&page=%s' % (str(category_id), sort_criteria, str(page_num)))

    return response

def get_html_data(html, tag, attribute):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(tag)

    id_list = []
    for element in elements:
        if element.attrs.get(attribute, None):
            proj_data = json.loads(element.attrs.get(attribute))
            id_list.append({'id': proj_data.get('id'), 'slug': proj_data.get('slug')})

    return id_list
