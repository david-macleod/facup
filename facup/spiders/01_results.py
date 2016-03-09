import scrapy
import pandas as pd
from scrapy.shell import inspect_response
from facup.items import ResultsItem
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader

fa_url = 'http://www.thefa.com/api/sitecore/Competitions/PastResultsRoundMatches'

years_csv = pd.read_csv('years_edit.csv')
round_ids = years_csv['round_id'].tolist()

class Results(scrapy.Spider):

	name = "results"
	
	def start_requests(self): #overide default requests method
		for round_id in round_ids:
			self.round_id = round_id
			yield FormRequest(url = fa_url, 
										callback=self.parse, 
										formdata={'roundId':str(round_id), 'page':'0'},
										meta={'round_id':round_id}) #passing round_id with request

	
	def parse(self, response):
		#inspect_response(response, self)
		round = ItemLoader(item = ResultsItem(), response=response)
		round.add_xpath('home_team', '//td[@class="cThree"]', re='>.*<')
		round.add_xpath('away_team', '//td[@class="cFive"]', re='>.*<')
		round.add_xpath('home_score', '//td[@class="cFour"]/text()')
		round.add_xpath('away_score', '//td[@class="cFour"]/text()')
		round.add_xpath('date', '//td[@class="cOne first"]/text()')
		round.add_xpath('replay', '//td[@class="cTwo"]')
		round.add_xpath('match_id', '//td[@class="last"]/a/@rel')
		round = round.load_item()
		
		match_count = len(round.values()[0]) #number of matches in round
			
		for i in range(match_count):
			match = {} #create new item for each match
			for key, value in round.items():
				match[key] = value[i]
				match['round_id'] = response.meta['round_id']
			yield match 