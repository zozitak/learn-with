#!/usr/bin/env python

import pandas as pd
import sqlite3

#redout to pandas dataframe 
table_materials = pd.read_excel(r'E:\\programing\\learn\\2023_02_07\\dummy2.xlsx', sheet_name='Materials')
table_properties = pd.read_excel(r'E:\\programing\\learn\\2023_02_07\\dummy2.xlsx', sheet_name='Properties')

#print(table_materials)
#print(table_properties)

#sqlite connection
con = sqlite3.connect('2023_02_07\\data.db')

#write pandas dataframe to sqllite database tables
table_materials.to_sql("material_table", con, if_exists="replace")
table_properties.to_sql("properties_table", con, if_exists="replace")

con.close()