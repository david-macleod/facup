import scrapy
import pandas as pd
from scrapy.shell import inspect_response
from facup.items import ResultsItem
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader

fa_url = 'http://www.thefa.com/api/sitecore/Competitions/PastResultsRoundMatches'

years_csv = pd.read_csv(r'C:\Users\David\Python\scrapy\facup\00_fa_cup\years_edit.csv')
round_ids = years_csv['round_id'].tolist()

class Resultsmiss(scrapy.Spider):

	name = "results_miss"
	
	def start_requests(self): #overide default requests method
		for round_id in ['10693']:
			self.round_id = round_id
			yield FormRequest(url = fa_url, 
										callback=self.parse, 
										formdata={'roundId':str(round_id), 'page':'0'},
										meta={'round_id':round_id}) #passing round_id with request
										
	# def start_requests(self): #overide default requests method
		# year_rq = FormRequest(
							# url = 'http://www.thefa.com/api/sitecore/Competitions/GetPastResultsForSeason',
							# callback=self.parse, 
							# formdata={'competitionSeasonId':'71236', 'competitionId':'1'}
							# )

	
	def parse(self, response):
		inspect_response(response, self)
		round = ItemLoader(item = ResultsItem(), response=response)
		round.add_xpath('home_team', '//td[@class="cThree"]', re='>.*<')
		round.add_xpath('away_team', '//td[@class="cFive"]', re='>.*<')
		round.add_xpath('home_score', '//td[@class="cFour"]/text()')
		round.add_xpath('away_score', '//td[@class="cFour"]/text()')
		round.add_xpath('date', '//td[@class="cOne first"]/text()')
		round.add_xpath('replay', '//td[@class="cTwo"]')
		round.add_xpath('match_id', '//td[@class="last"]/a/@rel')
		round = round.load_item()
		print round
		
		match_count = len(round.values()[0])
			
		for i in range(match_count):
			if round['home_score'][i] == 'NaN': #changed this to pick up missing scorelines
				match = {} #create new item for each match
				for key, value in round.items():
					match[key] = value[i]
					match['round_id'] = response.meta['round_id']
				yield match 