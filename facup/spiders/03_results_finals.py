import scrapy
import pandas as pd
import numpy as np
from scrapy.shell import inspect_response
from facup.items import ResultsFinalItem
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader

fac = pd.read_csv('C:/Users/David/Python/scrapy/facup/facup_archive.csv')

finals = fac[(fac['round'] == 'Final') & (fac['replay'] == False)]['year_id'].values #array of years with finals
years_series = fac.groupby('year')['year_id'].max()  #series of all year_ids indexed by year
missing_finals = years_series[~(years_series.isin(finals))]  #find years not in finals array and filter 


class ResultsFinals(scrapy.Spider):

	name = "results_finals"
	
	def start_requests(self): #overide default requests method
		for year, year_id in missing_finals.iteritems(): #iterate through series object
			yield FormRequest(
					url = 'http://www.thefa.com/api/sitecore/Competitions/GetPastResultsForSeason', 
					callback=self.parse, 
					formdata={'competitionSeasonId':str(year_id), 'competitionId':'1'},
					meta={'year_id':year_id, 'year':year,}
					) 

	
	def parse(self, response):
		#inspect_response(response, self)
		round = ItemLoader(item = ResultsFinalItem(), response=response)
		round.add_xpath('home_team', '//div[@class="mod-searchBarHistory-teamOne"]//figcaption/text()')
		round.add_xpath('away_team', '//div[@class="mod-searchBarHistory-teamTwo"]//figcaption/h4/text()')
		round.add_xpath(
		'home_score', '//div[@class="mod-searchBarHistory-gameDetails"]//p[@class="resultDetails"]/text()[1]'
		)
		round.add_xpath(
		'away_score', '//div[@class="mod-searchBarHistory-gameDetails"]//p[@class="resultDetails"]/text()[2]'
		)
		round.add_xpath('date', '//div[@class="mod-searchBarHistory-gameDetails"]/p[1]/text()')
		round = round.load_item()
		
		round['replay'] = False
		round['qualifier'] = False
		round['match_id'] = 0
		round['round_id'] = 0
		round['stage'] = 0
		round['round'] = 'Final'
		round['year_id'] = response.meta['year_id']
		round['year'] = response.meta['year']
		
		yield round