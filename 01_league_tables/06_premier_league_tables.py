#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import html5lib

#scraping premier league tables from 1993-2015 from wikipedia

tables_list = [] #list of tables, one for each year

def dup_cols(grp): #function to merge columns
    if grp.columns.size < 3:
        return grp.sum(axis=1)
    else:
        return grp.max(axis=1)			 

for year in range (1993, 2016):
	url = "https://en.wikipedia.org/wiki/%s-%s_Premier_League" % (str(year-1), str(year)[-2:])
	print year
	df_list = pd.read_html(url, match = 'Pts')
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
		df['tier'] = 11
		
		df.dropna(axis = 0, thresh=7, inplace=True) #drop NaN rows
		df['Pts'].replace(inplace=True, regex=True, to_replace=r'\D+', value='') #remove * and [] 
		df.dropna(axis=1, how = 'all', inplace=True) #remove NaN columns	
		df2 = df.convert_objects(convert_numeric=True, copy=False) #set numerical datatypes
		print df2
		df_m = df2.groupby(df.columns, axis=1).apply(dup_cols) # merge duplicate columns
		df_list_m.append(df_m)
	
	tables = pd.concat(df_list_m, ignore_index = True) 
	tables_list.append(tables) # table list is a concatenated datafram for each year
	
tables_df = pd.concat(tables_list, ignore_index = True)
path = r'C:\Users\David\Python\scrapy\facup\01_league_tables\premier_league_v1.csv'
tables_df.to_csv(path, index = False, encoding = 'utf-8')