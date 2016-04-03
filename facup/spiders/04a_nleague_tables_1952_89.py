import scrapy
import pandas as pd
from io import StringIO
from scrapy.shell import inspect_response
import re

url = 'http://www.nonleaguematters.co.uk/nonleaguetables/lt%s-%s.html'

url_list = [url % (year - 1, year) for year in range(1952, 1990)]

years_tables = [] #create an empty list to fill with the results of each parsed response


class Tables1952_89(scrapy.Spider):

	name = "tables1952_89"
	
	start_urls = url_list

	def parse(self, response):
		#return year from url
		year = response.url[57:61]
		
		# print duplicate leagues
		league_list = response.xpath('//p[@class="contents"]/a/text()').extract()
		checked = set()
		dupes = []
		for league in league_list:
			if league in checked:
				dupes.append(league)
			else:
				checked.add(league)
		print year, dupes
		
		#parse tables and store in dataframes
		year = response.url[57:61]
		tables = response.xpath('//pre/text()').extract()
		leagues = response.xpath('//p[@class="lgname"]/a[1]/text()').extract()
		
		df_list = []
		for table in tables:
			df_list.append(pd.read_fwf(StringIO(table), header = 1, widths=[3,31,3,3,3,3,4,4,4]))
		
		for x, df in enumerate(df_list):
			df['league'] = leagues[x]
			df['year'] = year
		year_tables = pd.concat(df_list)
		if year < 1989:
			years_tables.append(year_tables)
		else:
			years_tables.append(year_tables)
			cat = pd.concat(years_tables)
			cat.to_csv(r'C:\Users\David\Python\scrapy\facup\01_league_tables\nonleague_1952-89.csv', index = False)
			#csv manually edited to v2 to drop duplicate leagues preferentially and fix incorrect league names
			# correct league names checked here http://fchd.info/lghist/lghistsummary.htm
			