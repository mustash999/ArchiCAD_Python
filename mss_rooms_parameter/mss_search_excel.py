
import sys
import os
import subprocess
try:
	import pandas as pd
	import openpyxl
except ImportError:
	subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
	subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
	import pandas as pd
	import openpyxl



def mss_srch_xcl(excel_file, search_string):
	# Read the Excel file into a DataFrame
	df = pd.read_excel(excel_file)

	# Look for the search string in column 'A' and get the corresponding value from column 'B'
	result = df[df['Zone Number'] == search_string]['RTB Reference']
	
	if not result.empty:
		return result.iloc[0]  # Return the first matched value from column 'B'
	else:
		return None  # Return None if no match is found

# Test the function
print(mss_srch_xcl('list.xlsx', 'P 101'))

