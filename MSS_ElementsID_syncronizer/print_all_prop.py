from archicad import ACConnection
import os

conn = ACConnection.connect()
assert conn

acc = conn.commands
property_names = acc.GetAllPropertyNames()
file_path = os.path.join(os.path.expanduser("~"), "property_names.txt")

print(f"{len(property_names)} property names have been found.")
print(f"{property_names[:5]}")
with open(file_path, "w") as file:
    for name in property_names:
        print(name)
        file.write(f"{name}\n")

print(f"Property names have been saved to {file_path}")
