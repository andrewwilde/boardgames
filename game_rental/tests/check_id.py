from games.xml_parser import *

ID = 2

xml = get_xml_by_id(ID)

name = get_name(xml)
year = get_year(xml)
min_players = get_min_players(xml)
max_players = get_max_players(xml)
description = get_description(xml)
geek_rating = get_geek_rating(xml)
avg_rating = get_avg_rating(xml)
ranking = get_ranking(xml)

print "id #%i name is %s" % (ID, name)
print "id #%i year is %s" % (ID, year)
print "id #%i min players is %s" % (ID, min_players)
print "id #%i max players is %s" % (ID, max_players)
print "id #%i description is %s" % (ID, description)
print "id #%i geek rating is %s" % (ID, geek_rating)
print "id #%i average rating is %s" % (ID, avg_rating)
print "id #%i ranking is %s" % (ID, ranking)











