from archicad import ACConnection

conn = ACConnection.connect()
assert conn
acc = conn.commands
act = conn.types
acu = conn.utilities

if not conn:
	raise Exception("Failed to connect to ArchiCAD")

elm_id = acu.GetBuiltInPropertyId("General_ElementID")
elm_hgt =acu.GetBuiltInPropertyId("General_Height")
elm_wdt =acu.GetBuiltInPropertyId("General_Width")
elm_prt =acu.GetBuiltInPropertyId("General_LibraryPartName")


def ext_all_of_type(type):
	doors = acc.GetElementsByType(type)
	return doors

def mss_extract_props(door):
	prop_extraction = {}
	door_props = acc.GetPropertyValuesOfElements([door], [elm_id, elm_hgt, elm_wdt, elm_prt])[0].propertyValues
	prop_extraction["General_LibraryPartName"] = door_props[3].propertyValue.value
	prop_extraction["General_Width"] = door_props[2].propertyValue.value
	prop_extraction["General_Height"] = door_props[1].propertyValue.value
	prop_extraction["General_ElementID"] = door_props[0].propertyValue.value

	return prop_extraction

def set_openning_id(door, new_id):
	acc.SetPropertyValuesOfElements([act.ElementPropertyValue(door.elementId, elm_id, act.NormalStringPropertyValue(new_id))])

"""
for door in acc.GetElementsByType("Door"):
	i+=1
	door_props = acc.GetPropertyValuesOfElements([door], [elm_id, elm_hgt, elm_wdt, elm_prt])[0].propertyValues
	print(door_props[0].propertyValue.value)
	acc.SetPropertyValuesOfElements([act.ElementPropertyValue(door.elementId, elm_id, act.NormalStringPropertyValue(f"D{i:02d}"))])
	print(door_props[1].propertyValue.value)
	print(door_props[2].propertyValue.value)
	print(door_props[3].propertyValue.value)
"""