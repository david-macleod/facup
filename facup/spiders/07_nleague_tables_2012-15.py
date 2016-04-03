import scrapy
from scrapy.http import Request
from scrapy.shell import inspect_response


years = {1:2012,
			   2:2013,
			   3:2014,
			   4:2015}
leagues = {1:[501, 'National'], 
          2:[601, 'National North'], 
          3:[602, 'National South'],
          4:[701, 'Northern Premier Premier'],
          5:[801, 'Northern Premier Div One North'],
          6:[802, 'Northern Premier Div One South'],
          7:[702, 'Southern Premier'],
          8:[803, 'Southern Div One Central'],
          9:[804, 'Southern Div One South & West'],
          10:[703, 'Isthmian Premier'],
          11:[805, 'Isthmian Div One North'],
          12:[805, 'Isthmian Div One South'],
          13:[901, 'North West Counties Premier'],
          14:[902, 'Northern Counties East Premier'],
          15:[903, 'Northern Div One'],
          16:[904, 'Western Premier'],
          17:[905, 'Wessex Premier'],
          18:[906, 'Southern Combination Premier'],
          19:[907, 'Hellenic Premier'],
          20:[908, 'ZX Midland Football Alliance'],
          21:[909, 'United Counties Premier'],
          22:[910, 'Eastern Counties Premier'],
          23:[911, 'Southern Counties East'],
          24:[912, 'Spartan South Midlands Premier'],
          25:[913, 'Combined Counties Premier'],
          26:[914, 'Essex Senior'],
          27:[1001, 'Combined Counties Div One'],
          28:[1002, 'Eastern Counties Div One'],
          29:[1003, 'East Midlands Counties'],
          30:[1004, 'Hellenic Div One East'],
          31:[1005, 'Hellenic Div One West'],
          32:[1006, 'ZX Midland Combination Premier'],
          33:[1007, 'Northern Counties East Div One'],
          34:[1008, 'Northern Div Two'],
          35:[1009, 'North West Counties Div One'],
          36:[1010, 'South West Peninsula Premier'],
          37:[1011, 'Spartan South Midlands Div One'],
          38:[1012, 'Southern Combination Div One'],
          39:[1013, 'Wessex Div One'],
          40:[1014, 'Western Div One'],
          41:[1015, 'West Midlands Regional Premier'],
          42:[1016, 'United Counties Div One'],
          161:[1017, 'Kent Invicta'],
          214:[915, 'Midland Premier'],
          215:[1018, 'Midland Div One']}
		  
url_list = []
		  
for year in years.keys():
	for league in leagues.keys():
		url = 'http://www.nonleaguematters.co.uk/divisions/%s/%s/' % (league, year)
		url_list.append(url)
		
		
class Nlt1(scrapy.Spider):
	
	name = 'nlt1'
	start_urls = url_list
	
	
	def parse(self, response):
		lg = int(response.url.split('/')[-3])  #extracting "league" from url
		yr = int(response.url.split('/')[-2])  #extracting "year" from url
		sel = response.xpath('//table[@class="league"]')
		nrows =  len(sel.xpath('.//tr/td[1]/text()').extract())
		
		item = {}
		
		for row in range(nrows):
			item['rank'] = sel.xpath('.//tr/td[1]/text()').extract()[row]
			item['team'] = sel.xpath('.//tr/td[2]/text()').extract()[row]
			item['p'] = sel.xpath('.//tr/td[3]/text()').extract()[row]
			item['w'] = sel.xpath('.//tr/td[4]/text()').extract()[row]
			item['d'] = sel.xpath('.//tr/td[5]/text()').extract()[row]
			item['l'] = sel.xpath('.//tr/td[6]/text()').extract()[row]
			item['f'] = sel.xpath('.//tr/td[7]/text()').extract()[row]
			item['a'] = sel.xpath('.//tr/td[8]/text()').extract()[row]
			item['pts'] = sel.xpath('.//tr/td[20]/text()').extract()[row]
			item['tier'] = leagues[lg][0]
			item['league'] = leagues[lg][1]
			item['year'] = years[yr]
			yield item
			
			#export to nonleague_2012_15.csv
		