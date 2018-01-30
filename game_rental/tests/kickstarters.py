from kickstarters.extract import *
from kickstarters.category_id import TABLETOP_ID

html = get_kickstarter_html(TABLETOP_ID, 'popularity', 2).content

get_html_data(html, 'div', 'data-project')
