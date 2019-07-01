# It is the principal class
# The web scraper's main parameters are: 1) Token; 2) Platform (Android/iOS); 
# 3) Categories; 4) Keyword; 5) Search field (app's name or app's name+full despcription); and 6) The app's supported metalanguage 


# Libraries

import sys

import csvExport

import connection

import utils

import errors

# Platform can be either 'Android' or 'iOS'
platform = 'android'

# Keyword (separated by either blanks or by the following logic commands: OR/AND/NOT
keyword = 'diabetes OR mellitus'


# App categories (separated by commas)
categories = 'MEDICAL, LIFESTYLE, EDUCATION, HEALTH_AND_FITNESS'

# Token of 42Matters 
token = '6dc3eba38263b374e06986f69c876c3ea6cb2f9f'  

# App's metadata language (all languages if argument is in blank) 
langs = 'en'

con = connection.Connection()
con.set_categories(categories)
con.set_keyword(keyword)
con.set_langs(langs)
con.set_os(platform)
con.set_token(token)

data = con.get_data()

utils = utils.Utils()
result = utils.parseData(data)

csv_file_name = 'result.csv'
csv_export = csvExport.csvExport()
csv_export.set_file_name(csv_file_name)
csv_export.write_to_csv(result)
