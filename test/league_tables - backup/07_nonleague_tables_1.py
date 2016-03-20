import pandas as pd
import numpy as np

years = [1,2,3,4,5]

tables_list = []

for year in years:
	url = 'http://www.nonleaguematters.co.uk/divisions/1/%s/' % year
	df = pd.read_html(url, match = 'Overall', header = 1)[0]
	df.dropna(axis = 0, how='any')
	tables_list.append(df)

print pd.concat(tables_list)