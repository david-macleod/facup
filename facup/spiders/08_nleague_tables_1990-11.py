#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy
import html5lib
import re

#scraping non-league league tables from 1990-2011 from wikipedia using pandas read_html

#creating a dictionary of league to be added to scraped data frames
# start by creating a dicitionary full of years as keys and empty dictionaries as items
leagues = {year: {} for year in range(1990, 2012)}

	#adding SOUTHERN LEAGUE names to dictionary
for year in range(1990, 2000):
	leagues[year]['SOUTHERN FOOTBALL LEAGUE'] = ['PREMIER DIVISION', 'MIDLAND DIVISION', 'SOUTHERN DIVISION']
for year in range(2000, 2007):
	leagues[year]['SOUTHERN FOOTBALL LEAGUE'] = ['PREMIER DIVISION', 'EAST DIVISION', 'WEST DIVISION']
for year in range(2007, 2010):
	leagues[year]['SOUTHERN FOOTBALL LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE MIDLANDS', 'DIVISION ONE SOUTH & WEST']
for year in range(2010, 2012):
	leagues[year]['SOUTHERN FOOTBALL LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE CENTRAL', 'DIVISION ONE SOUTH & WEST']
	
	#adding NORTHERN LEAGUE names to dictionary
for year in range(1990, 2008):
	leagues[year]['NORTHERN PREMIER LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE']
for year in range(2008, 2012):
	leagues[year]['NORTHERN PREMIER LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE NORTH', 'DVISION ONE SOUTH']	

	#adding CONFERENCE LEAGUE names to dictionary
for year in range(1990, 2005):
	leagues[year]['FOOTBALL CONFERENCE'] = ['']
for year in range(2005, 2012):
	leagues[year]['FOOTBALL CONFERENCE'] = ['', 'NORTH', 'SOUTH']	

	#adding ISTHMIAN LEAGUE names to dictionary	
for year in range(1990, 1992):
	leagues[year]['ISTHMIAN LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE', 'DIVISION TWO NORTH', 'DIVISION TWO SOUTH']
for year in range(1992, 2003):
	leagues[year]['ISTHMIAN LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE', 'DIVISION TWO', 'DIVISION THREE']
for year in range(2003, 2005):
	leagues[year]['ISTHMIAN LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE NORTH', 'DIVISION ONE SOUTH', 'DIVISION TWO']	
for year in range(2005, 2007):
	leagues[year]['ISTHMIAN LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE', 'DIVISION TWO']
for year in range(2007, 2012):
	leagues[year]['ISTHMIAN LEAGUE'] = ['PREMIER DIVISION', 'DIVISION ONE NORTH', 'DIVISION ONE SOUTH']	

df_list_all = [] #super list with all df joined!
	
# WIKIPEDIA LEAGUE SCRAPING
def table_scraper(league_url):
	for year in range (1990, 2012): 
		league = league_url.replace('_', ' ').upper() #strip underscores and convert to upper case
		#year 2000 has different format on URL
		if year == 2000:
			url = 'https://en.wikipedia.org/wiki/1999-2000_%s' % league_url
		else:
			url = 'https://en.wikipedia.org/wiki/%s–%s_%s' % (str(year-1), str(year)[-2:], league_url)
		print year
		#returns a list of dataframes, each one containing an html table contatining 'Pts'
		df_list = pd.read_html(url, match = 'Pts', header = 0) 
		
		for i, df in enumerate(df_list):
			league_name =  ' '.join([league, leagues[year][league][i]])
			#creating year and league columns
			df['year'] = year
			df['league'] = league_name
			df_list_all.append(df) # add to the super list!

table_scraper('Northern_Premier_League')			
table_scraper('Southern_Football_League')
table_scraper('Football_Conference')
table_scraper('Isthmian_League')

leagues_cat = pd.concat(df_list_all, ignore_index = True)

leagues_cat.to_csv(r'C:\Users\David\Python\scrapy\facup\01_league_tables\nonleague_1990-11.csv', index = False, encoding = 'utf-8')
		
		
		
