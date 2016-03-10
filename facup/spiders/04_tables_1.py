import scrapy
import pandas as pd
from io import StringIO
from scrapy.http import Request
import re

class Tables1(scrapy.Spider):

	name = "tables1"
	
	def start_requests(self):
		for year in range (1991, 1992):
			url = "http://www.rsssf.com/engpaul/fla/%s-%s.html" % (str(year), str(year + 1)[-2:])
			yield Request(url = url,
									callback=self.parse, 
									meta={'year': year + 1})
	
	def parse(self, response):
		table_list = response.xpath('//pre/text()').extract()
		for table in table_list: #iterate through list of tables
			if len(table) > 2: #exclude empty "tables"
				for i, row in enumerate(StringIO(table)): #iterate through each row of table 'file'
					row_split = row.split() #split each row into list of strings
					if len(row_split) and row_split[0].strip('.') == '1':  #testing if row an empty list and 1st item = 1
						start = i

				df = pd.read_fwf(
					StringIO(table),
					skiprows = start - 2,
					header = 1)	
				print df
				

			
			#merge columns
			#df['W'] = df['W'] + df['W.1'] 
			#df['D'] = df['D'] + df['D.1']
			#df['L'] = df['L'] + df['L.1']
			#df['F'] = df['F'] + df['F.1']
			#df['A'] = df['A'] + df['A.1']			
			#df.drop(['W.1', 'D.1', 'L.1', 'F.1', 'A.1'], axis=1, inplace = True)
			
			#df['year'] = response.meta['year']
			


				
				
				

