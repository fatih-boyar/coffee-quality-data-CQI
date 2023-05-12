import pandas as pd
import numpy as np
import os

# There must be 5 tables for each coffee. Some of them skipped and could not scrape the tables.
# Might be a slow loading of the page and missed the click on coffee ID link.

# all the files from working directory:
dir = pd.DataFrame({'files': os.listdir()})

# only the files we scraped from the database
coffee_list = dir[dir['files'].str.contains('coffee')].reset_index(drop=True)

# splitting the file names so we can see the table names
coffee_list_split_temp = coffee_list['files'].str.split('_', 2, expand=True)
col1 = coffee_list_split_temp[0] + '_' + coffee_list_split_temp[1]

coffee_list_split = pd.DataFrame({'coffee': col1,
                                     'tables': coffee_list_split_temp[2]})

# see which coffees do not have 5 tables
table_counts = coffee_list_split.groupby('coffee').count()
print(table_counts[table_counts['tables'] != 5])

# They are coffee_135, coffee_185 and coffee_85
# Seems like the program could not click on coffee id and saved the outer table.
# This might change from case to case but if you follow the same steps you can replicate with yours

# we can skip these coffee numbers and gather other tables.

df_list = []
# 87 turned out weird, figure out what happened here
skips = [85, 135, 185]


for i in range(210):
	if i in skips:
		print('skipping {}'.format(i))
		pass
	else:
		df0 = pd.read_csv('coffee_{}_table_0.csv'.format(i))
		df1 = pd.read_csv('coffee_{}_table_1.csv'.format(i))
		df2 = pd.read_csv('coffee_{}_table_2.csv'.format(i))
		df3 = pd.read_csv('coffee_{}_table_3.csv'.format(i))
		df4 = pd.read_csv('coffee_{}_table_4.csv'.format(i))


		# df0: on the website, this table is used for links. Irrelevant for our aim so skipping this one.
		"""
		   Unnamed: 0                             89.33
		0         NaN             Q Arabica Certificate
		1         NaN                  Embeddable Image
		2         NaN  Cupping Protocol and Descriptors
		3         NaN       View Green Analysis Details
		4         NaN                  Request a Sample
		5         NaN                   Species Arabica
		6         NaN        Owner Coffee Quality Union
		"""

		# df1
		"""
		   Unnamed: 0                  0                      1                   2  \
		0           0  Country of Origin               Colombia      Number of Bags   
		1           1          Farm Name       Finca El Paraiso          Bag Weight   
		2           2         Lot Number             CQU2022015  In-Country Partner   
		3           3               Mill       Finca El Paraiso        Harvest Year   
		4           4         ICO Number                    NaN        Grading Date   
		5           5            Company   Coffee Quality Union               Owner   
		6           6           Altitude              1700-1930             Variety   
		7           7             Region         Piendamo,Cauca              Status   
		8           8           Producer  Diego Samuel Bermudez   Processing Method   
								 3  
		0                        1  
		1                    35 kg  
		2    Japan Coffee Exchange  
		3              2021 / 2022  
		4     September 21st, 2022  
		5     Coffee Quality Union  
		6                 Castillo    
		"""
		df1.columns = ['zero','one','two','three','four']
		colnames1 = df1['one'].tolist()
		colnames2 = df1['three'].tolist()
		data1 = df1['two'].tolist()
		data2 = df1['four'].tolist()

		df1_processed = pd.DataFrame([(data1+data2)], columns=(colnames1+colnames2))

		# df2: The cupping scores are stored in this table
		"""
		  Unnamed: 0           0     1                 2      3
		0           0       Aroma  8.58        Uniformity  10.00
		1           1      Flavor  8.50         Clean Cup  10.00
		2           2  Aftertaste  8.42         Sweetness  10.00
		3           3     Acidity  8.58           Overall   8.58
		4           4        Body  8.25           Defects   0.00
		5           5     Balance  8.42  Total Cup Points  89.33
		"""
		df2.columns = ['zero','one','two','three','four']
		colnames1 = df2['one'].tolist()
		colnames2 = df2['three'].tolist()
		data1 = df2['two'].tolist()
		data2 = df2['four'].tolist()

		df2_processed = pd.DataFrame([(data1+data2)], columns=(colnames1+colnames2))

		# df3
		"""
		   Unnamed: 0                     0               1                     2  \
		0           0              Moisture          11.8 %                 Color   
		1           1  Category One Defects  0 full defects  Category Two Defects   
		2           2               Quakers               0                   NaN   
						3  
		0           Green  
		1  3 full defects  
		2             NaN    
		"""

		df3.columns = ['zero','one','two','three','four']
		colnames1 = df3['one'].tolist()
		colnames2 = df3['three'].tolist()
		data1 = df3['two'].tolist()
		data2 = df3['four'].tolist()

		df3_processed = pd.DataFrame([(data1+data2)], columns=(colnames1+colnames2))

		# df4
		"""
		   Unnamed: 0                      0  \
		0           0             Expiration   
		1           1     Certification Body   
		2           2  Certification Address   
		3           3  Certification Contact   
														   1  
		0                               September 21st, 2023  
		1                              Japan Coffee Exchange  
		2  〒413-0002 静岡県熱海市伊豆山１１７３−５８ 1173-58 Izusan, Ata...  
		3            松澤　宏樹　Koju Matsuzawa - +81(0)9085642901    
		"""

		df4.columns = ['zero','one','two']
		colnames1 = df4['one'].tolist()
		data1 = df4['two'].tolist()

		if i > 1:
			prev_cols = df.columns # cols before replacing df with next coffee

		df4_processed = pd.DataFrame([data1], columns=colnames1)
		df = pd.concat([df1_processed, df2_processed, df3_processed, df4_processed],1)
		df = df.rename(columns={np.nan: "NA"})
		df_list.append(df)
		print(i)

		these_cols = df.columns

		# are the columns matching across coffees? 
		if i > 1:
			# figuring out where the column mismatches are 
			#print(these_cols==prev_cols)
			#print(these_cols)
			#print(prev_cols)
			pass


j = 0
for i in df_list:
	print('{} shape: {}'.format(j,i.shape))
	j+=1
# df_list stores all the dataframes. Each data frame is in 1 row 40 column shape

df_final = pd.concat(df_list, 0)
print(df_final.columns)
print(df_final.shape)
print(df_final.head())
df_final.to_csv('df_1_arabica.csv')
