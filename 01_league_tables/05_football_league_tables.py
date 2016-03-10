#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import html5lib

#scraping football league tables from 1947-2015 from wikipedia
#does not include tier 1.1 (Premier League) from 1993 onwards

#defining tiers based on order each league with appear on webpage
tiers = {1947: [11, 21, 31, 32],
			 1959: [11, 21, 31, 41],
			 1993: [21, 31, 41]}

tables_list = [] #list of tables, one for each year

def dup_cols(grp): #function to merge columns
    if grp.columns.size < 3:
        return grp.sum(axis=1)
    else:
        return grp.max(axis=1)			 

for year in range (1947, 2016):
	if year == 2000: #2000 has a different url format
		url = "https://en.wikipedia.org/wiki/1999-2000_Football_League"
	elif year == 2013: #2013 has a different url format
		url = "https://en.wikipedia.org/wiki/2012–13_Football_League"
	else: 
		url = "https://en.wikipedia.org/wiki/%s-%s_Football_League" % (str(year-1), str(year)[-2:])
		
	df_list = pd.read_html(url, match = 'Pts')
	print year
	df_list_m = [] #empty list to store munged df_list
	
	#looping through dataframe list  to find header row
	for i, df in enumerate(df_list):
		if df[0].isnull().max(): #testing if there is a NaN value in the first column
			df.columns = df.iloc[1]
			df.drop(df.index[0:2], inplace = True)
		else:
			df.columns = df.iloc[0]
			df.drop(df.index[0:1], inplace = True)
			
	#creating new colums: year, tier
		df['year'] = year
		if year in range(1947,1959):
			df['tier'] = tiers[1947][i]
		elif year in range(1959,1993):
			df['tier'] = tiers[1959][i]
		elif year in range(1993,2016):
			df['tier'] = tiers[1993][i]

		df['Pts'].replace(inplace=True, regex=True, to_replace=r'\D+', value='') #remove * and [] 
		df.dropna(axis=1, how = 'all', inplace=True) #remove NaN columns	
		df2 = df.convert_objects(convert_numeric=True, copy=False) #set numerical datatypes
		df_m = df2.groupby(df.columns, axis=1).apply(dup_cols) # merge duplicate columns
		df_list_m.append(df_m)
	
	tables = pd.concat(df_list_m, ignore_index = True)
	tables_list.append(tables)
	
tables_df = pd.concat(tables_list, ignore_index = True)
path = r'C:\Users\David\Python\scrapy\facup\01_league_tables\football_league_v1.csv'
tables_df.to_csv(path, index = False, encoding = 'utf-8')