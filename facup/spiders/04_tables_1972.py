import scrapy
import pandas as pd
from io import StringIO
from scrapy.shell import inspect_response
import re


class Tables1972(scrapy.Spider):

	name = "Tables1972"
	start_urls =['http://www.nonleaguematters.co.uk/nonleaguetables/lt1971-1972.html#top']

	def parse(self, response):
		tables = response.xpath('//pre/text()').extract()
		leagues = response.xpath('//p[@class="lgname"]/a[1]/text()').extract()
		print leagues
		df_list = [pd.read_fwf(StringIO(table), header = 1, widths=[3,31,3,3,3,3,4,4,4]) for table in tables]
		for x, df in enumerate(df_list):
			df['league'] = leagues[x]
		cat = pd.concat(df_list)
		cat.to_csv(r'C:\Users\David\Python\scrapy\facup\01_league_tables\nonleague_1972.csv', index = False)
		