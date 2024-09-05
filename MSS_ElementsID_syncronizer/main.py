import utils
import opennings_control as op
import table_control as table

from archicad import ACConnection
conn = ACConnection.connect()
assert conn
acc = conn.commands
act = conn.types
acu = conn.utilities

el_type = "Door" # "Window" or "Door"

all_opennings = op.ext_all_of_type(el_type)
file_path = "C:/00_MS_PSP/000_Tools/ArchiCAD/000_PY_4_ArchiCAD/MSS_Door_type_excel_sync/Doors.xlsx"
or_fd = table.read_excel_file(file_path)
fd = table.remove_duplicates(or_fd)

i = 0

for openning in all_opennings:
	trig = False
	i	+= 1
	openning_props = op.ext_obj_properties(openning)
	found= table.init_srch_df(fd, "Library Part Name", openning_props["General_LibraryPartName"])
	if found is not None:
		found = table.init_srch_df(found, "Width", openning_props["General_Width"])
		if found is not None:
			found = table.init_srch_df(found, "Height", openning_props["General_Height"])
			if found is not None:
				op.set_openning_id(openning, found["Element ID"].values[0])
				trig = True
	if not trig:
		print (f"door {i} not found in the excel file")
		new_entry = {"Library Part Name": openning_props["General_LibraryPartName"],
							"Width": openning_props["General_Width"],
							"Height": openning_props["General_Height"],
							"Element ID": "D05"}
		fd = table.add_entry_to_df(fd, new_entry)
		print(fd)
		print("New entry added")

print(f"Total {i} doors processed")
fd.to_excel(file_path, index=False)
print("Excel file updated")
	
 
		
		
	
