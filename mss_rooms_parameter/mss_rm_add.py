from archicad import ACConnection

conn = ACConnection.connect()
assert conn
acc = conn.commands
act = conn.types
acu = conn.utilities

if not conn:
	raise Exception("Failed to connect to ArchiCAD")

rm_num = acu.GetBuiltInPropertyId("Zone_ZoneName")
rtb_ref = acu.GetUserDefinedPropertyId("RTB Reference")


def ext_all_of_type(type):
	elements = acc.GetElementsByType(type)
	return elements

def mss_extract_props(element):
	prop_extraction = {}
	door_props = acc.GetPropertyValuesOfElements([element], [rm_num])[0].propertyValues
	prop_extraction["Zone_ZoneName"] = door_props[0].propertyValue.value
""" 
def mss_rtb_update(room, new_id):
	acc.SetPropertyValuesOfElements([act.ElementPropertyValue(room., elm_id, act.NormalStringPropertyValue(new_id))])

 """
