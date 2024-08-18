import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog

def mss_create_path(file_name):
	root = tk.Tk()
	root.withdraw()
	
	folder_path = filedialog.askdirectory(title="Select Folder to Save the File")

	if not folder_path:
		print("No folder selected. Operation cancelled.")
		return None

	# Construct the full file path
	file_path = os.path.join(folder_path, f"{file_name}s.xlsx")
	
	if not os.path.exists(file_path):
		df = pd.DataFrame(columns=["Library Part Name", "Width", "Height", "Element ID"])
		df.to_excel(file_path, index=False)
	print(f"File created at: {file_path}")
	return file_path

# Example usage
file_name = "example_file"
file_path = mss_create_path(file_name)
if file_path:
	print(f"File created at: {file_path}")


def read_excel_file(file_path):
	try:
		df = pd.read_excel(file_path)
		return df
	except FileNotFoundError:
		print(f"Error: The file '{file_path}' was not found.")
		return None
	except Exception as e:
		print(f"Error: An unexpected error occurred: {str(e)}")
		return None

def remove_duplicates(df):

	# Define the columns to check for duplicates
	columns_to_check = ["Library Part Name", "Width", "Height"]
	
	# Check if all required columns are in the DataFrame
	for col in columns_to_check:
		if col not in df.columns:
			raise ValueError(f"Column '{col}' not found in DataFrame")
	
	# Drop duplicates based on the specified columns
	df_no_duplicates = df.drop_duplicates(subset=columns_to_check)
	
	return df_no_duplicates


def mss_srch(df, column_name, search_value):
	matched_rows = df[df[column_name] == search_value]
	if not matched_rows.empty:
		return matched_rows
	else:
		return None

def mss_add_entry(df, entry):

	new_entry_df = pd.DataFrame([entry])
	df = pd.concat([df, new_entry_df], ignore_index=True)
	return df


"""
fd= read_excel_file("C:/00_MS_PSP/000_Tools/ArchiCAD/000_PY_4_ArchiCAD/MSS_Door_type_excel_sync/Opennings.xlsx")
s = "Tür Ol 1-Fl 26"

matched_rows = fd[fd["Library Part Name"] == s]

if not matched_rows.empty:
	print("True")
	print("Matched row(s):")
	print(matched_rows)
else:
	print("False")
	
print(fd)
"""