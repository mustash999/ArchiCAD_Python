import pandas as pd

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
    """
    Removes duplicate rows in a DataFrame based on the first three columns: 
    'Library Part Name', 'Width', and 'Height'.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: DataFrame with duplicates removed.
    """
    # Define the columns to check for duplicates
    columns_to_check = ["Library Part Name", "Width", "Height"]
    
    # Check if all required columns are in the DataFrame
    for col in columns_to_check:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")
    
    # Drop duplicates based on the specified columns
    df_no_duplicates = df.drop_duplicates(subset=columns_to_check)
    
    return df_no_duplicates


def init_srch_df(df, column_name, search_value):
	matched_rows = df[df[column_name] == search_value]
	if not matched_rows.empty:
		return matched_rows
	else:
		return None

def add_entry_to_df(df, entry):

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