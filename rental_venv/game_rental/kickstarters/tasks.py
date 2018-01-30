import requests

from extract  import *
from category_id import TABLETOP_ID
from models import KickStarter
from game_rental.celery import app

@app.task
def store_kickstarters():

    id_list = []
    page_num = 1
    while True:
        print "Checking page number %i" % page_num
        response = get_kickstarter_html(TABLETOP_ID, 'popularity', page_num)
        if response.status_code == 200:
            id_list = id_list + get_html_data(response.content, 'div', 'data-project')
            for item in id_list:
                KickStarter.objects.get_or_create(kickstarter_id=item.get('id'), defaults={'category_id': TABLETOP_ID, 'slug': item.get('slug')})
            page_num = page_num + 1
        else:
            print "response didn't return a 200 response. status=%s" % str(response.status_code)
            break


