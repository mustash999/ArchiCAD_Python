# **************************************************************************** #
#                                                                              #
#                                                                              #
#    main.py                                                                   #
#                                                                              #
#    By: Mustash <www.geniuspandatech.com>                                     #
#                                                                              #
#    Created: 2024/08/18 15:16:09 by Mustash                                   #
#    Updated: 2024/08/18 15:16:09 by Mustash                                   #
#                                                                              #
# **************************************************************************** #

# external imports
from archicad import ACConnection

conn = ACConnection.connect()
assert conn
acc = conn.commands
act = conn.types
acu = conn.utilities

# internal imports
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import opennings_control as op
import table_control as table
import ask
import utils


def main():
	
	#-------------------------------------------------------------Openning and cleaning Excel  file ----------------------------------------------
	file_path = f"MSS_ElementsID_syncronizer/output/{el_type}s.xlsx"
	or_fd = table.read_excel_file(file_path)
	fd = table.remove_duplicates(or_fd)



	#-------------------------------------------------------------Extracting the opennings and searching for them in the excel file----------------------------------------------
	el_type = ask.mss_type_select()
	i = 0
	all_opennings = op.ext_all_of_type(el_type)

	for openning in all_opennings:
		trig = False 											# trigger to check if the door is found in the excel file
		i	+= 1
		openning_props = op.mss_extract_props(openning)

		#--------------------------------------------------Searching for the openning in the excel file--------------------------------
		found= table.mss_srch(fd, "Library Part Name", openning_props["General_LibraryPartName"])
		if found is not None:
			found = table.mss_srch(found, "Width", openning_props["General_Width"])
			if found is not None:
				found = table.mss_srch(found, "Height", openning_props["General_Height"])
				if found is not None:
					op.set_openning_id(openning, found["Element ID"].values[0])
					trig = True # ----------->>>> door found in the excel file trigger set to True
		if not trig:
			print (f"door {i} not found in the excel file")
			new_entry = {"Library Part Name": openning_props["General_LibraryPartName"],
								"Width": openning_props["General_Width"],
								"Height": openning_props["General_Height"],
								"Element ID": "D05"}
			fd = table.mss_add_entry(fd, new_entry)
			print(fd)
			print("New entry added")

	print(f"Total {i} doors processed")
	fd.to_excel(file_path, index=False)
	print("Excel file updated")
	
 
		
		
	
