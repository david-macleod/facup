import scrapy
from scrapy.loader.processors import Compose
import re
import HTMLParser


#returning full node rather than text() so need to test for replays
def replay(matches):
	for i, match in enumerate(matches):
		if '(R)' in match:
			matches[i] = True
		else:
			matches[i] = False
	return matches
	
#removing > and < from team names	and escaping html &amp; from teams inlcuding ampersand
def teamname_strip(teams):
	return [HTMLParser.HTMLParser().unescape(team[1:-1]) for team in teams]

	
#testing if scoreline is missing then stripping home and away goals	
def test_int(x):
	try:
		int(x)
		return int(x)
	except ValueError:
		return ''
	
def home_goals(scores):
	goals = [test_int(score[:2]) for score in scores]
	return goals

	
def away_goals(scores):
	goals = [test_int(score[-2:]) for score in scores]
	return goals

			

class ResultsItem(scrapy.Item):
	home_team = scrapy.Field(input_processor = Compose(teamname_strip))
	away_team = scrapy.Field(input_processor = Compose(teamname_strip))
	home_score = scrapy.Field(input_processor = Compose(home_goals))
	away_score = scrapy.Field(input_processor = Compose(away_goals))
	date = scrapy.Field()
	replay = scrapy.Field(input_processor = Compose(replay))
	match_id = scrapy.Field()
	
	
class YearItem(scrapy.Item):
	round = scrapy.Field()
	round_id = scrapy.Field()
	stage = scrapy.Field()
	year = scrapy.Field()
	year_id = scrapy.Field()
	
	
class ResultsFinalItem(scrapy.Item):
	home_team = scrapy.Field()
	away_team = scrapy.Field()
	home_score = scrapy.Field()
	away_score = scrapy.Field()
	date = scrapy.Field()
	replay = scrapy.Field()
	match_id = scrapy.Field()
	round_id = scrapy.Field()
	round = scrapy.Field()
	year_id = scrapy.Field()
	year = scrapy.Field()
	stage = scrapy.Field()
	qualifier = scrapy.Field()
	
