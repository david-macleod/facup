import scrapy
from scrapy.shell import inspect_response
from facup.items import YearItem
from scrapy.http import FormRequest


fa_url = 'http://www.thefa.com/api/sitecore/Competitions/PastResultsRoundMatches'

class Results(scrapy.Spider):

	name = "id"
	start_urls =['http://www.thefa.com/thefacup/more/pastresults#']
	
	def parse(self, response):
		#inspect_response(response, self)
		r = response.xpath('//dd//option')
		ids = {}
		year_id = r.xpath('@value').extract() #extract year ids as a list
		year = r.xpath('text()').extract() # extract years as a list
		for i, yr in enumerate(year):
			year[i] = yr.strip()[-4:] # remove whitespace and slice final 4 chars
		
		id_db = dict(zip(year_id, year)) # zip lists together and create dict
		# start new round of requests to obtain season ids
		year_url = 'http://www.thefa.com/api/sitecore/Competitions/GetPastResultsForSeason'
		
		for yr in id_db:
			year_rq = FormRequest(
							url = year_url, 
							callback=self.year_parse, 
							formdata={'competitionSeasonId':yr, 'competitionId':'1'}
							)
			#packing year and year_id so we can access them in the next request
			year_rq.meta['year'] = id_db[yr]
			year_rq.meta['year_id'] = yr
			yield year_rq
		
	def year_parse(self, response):
		r = response.xpath('//div[@class="gTable-title"]')
		round_ids = r.xpath('@data').extract() #extracting round ids for year
		round_names = r.xpath('./h4/a/text()').extract() #extracting round names for year
		
		for i, rnd in enumerate(round_ids):
			item = YearItem()
			item['year'] = response.meta['year']
			item['year_id'] = response.meta['year_id']
			item['round_id'] = rnd
			item['round'] = round_names[i]
			item['stage'] = len(round_ids) - i 
			yield item
		
		
		
		
		
		
		
		
		