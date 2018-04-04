import requests

from .extract  import *
from .category_id import TABLETOP_ID
from .models import KickStarter
from game_rental.celery import app

@app.task
def store_kickstarters(sort_category, record_count):
    """
    sort_category should be one of the following:
        popularity
        newest
        end_date
        most_funded
        most_backed
    """
    id_list = []
    page_num = 1
    KickStarter.objects.filter(sort_category=sort_category).delete()
    while True:
        print("Checking page number %i" % page_num)
        response = get_kickstarter_html(TABLETOP_ID, sort_category, page_num)
        if response.status_code == 200:
            id_list = id_list + get_html_data(response.content, 'div', 'data-project')
            for item in id_list:
                KickStarter.objects.get_or_create(kickstarter_id=item.get('id'), defaults={'category_id': TABLETOP_ID, 'slug': item.get('slug'), 'sort_category': sort_category})
                if KickStarter.objects.filter(sort_category=sort_category).count() >= record_count:
                    return
            page_num = page_num + 1
        else:
            return



