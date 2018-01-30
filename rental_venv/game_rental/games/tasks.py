import requests

from game_rental.celery import app
from xml_parser import *
from models import BoardGame

@app.task
def scan_boardgames():
    collect_game_data('boardgame')

@app.task
def scan_expansions():
    collect_game_data('boardgameexpansion')

def collect_game_data(type):
    REGISTERED_FUNCS = [ ('name', get_name),
                         ('year_published', get_year),
                         ('min_players', get_min_players),
                         ('max_players', get_max_players),
                         ('description', get_description),
                         ('geek_rating', get_geek_rating),
                         ('average_rating', get_avg_rating),
                         ('ranking', get_ranking) ]
    MAX_ID = 200000
    CHUNK_SIZE = 100
    current_id = 1
    bg_num = 1
    while current_id < MAX_ID:
        id_str = [str(i) for i in range(current_id, current_id + 100)]
        try:
            game_xml = get_xml_by_id(','.join(id_str), type)
        except Exception as e:
            print "XML not retrievable. e=%s" % str(e)
            continue       

        for item in game_xml.iter('item'):
            game_dict = {}
            for func in REGISTERED_FUNCS:
                game_dict[func[0]] = func[1](item)
       
            if game_dict:
                try:
                    BoardGame.objects.get_or_create(**game_dict)
                    print "#%i Created a BoardGame object for %s" % (bg_num, game_dict.get('name'))
                    bg_num = bg_num + 1
                except Exception as e:
                    print "Unable to get or create boardgame object for %s" % game_dict.get('name')
 
        current_id = current_id + CHUNK_SIZE

