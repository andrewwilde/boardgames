import requests
import time
from xml.etree import ElementTree

def get_xml_by_id(id, type):
    response = requests.get("https://boardgamegeek.com/xmlapi2/things?type=%s&stats=1&id=%s" % (type, str(id)))
    try:
        root = ElementTree.fromstring(response.content)
        return root
    except Exception as e:
        logger.error("Unable to parse response XML. e=" + str(e))

    return None

def get_name(xml):
    return get_xml_val(xml, 'name')

def get_year(xml):
    return get_xml_val(xml, 'yearpublished')

def get_min_players(xml):
    return get_xml_val(xml, 'minplayers')

def get_max_players(xml):
    return get_xml_val(xml, 'maxplayers')

def get_description(xml):
    for item in xml.iter('description'):
        try:
            return item.text
        except Exception as e:
            print "Failed to get description"
            return "None"

def get_geek_rating(xml):
    return get_xml_val(xml, 'bayesaverage')

def get_avg_rating(xml):
    return get_xml_val(xml, 'average')

def get_ranking(xml):
    ranking = get_xml_val(xml, 'rank')
    try:
        return int(ranking)
    except:
        return -1

def get_xml_val(xml, tag):
    for item in xml.iter(tag):
        try:
            return item.attrib.get('value')
        except Exception as e:
            print "Failed to get %s" % tag
            return "None"

def get_xml_iter(xml, attribute):
    return xml.iter(attribute)
