import json

# Load the JSON data
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Extract interface details
interfaces = data["imdata"]

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

# Print interface details
for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "").ljust(20)
    speed = attributes.get("speed", "inherit").ljust(6)
    mtu = attributes.get("mtu", "").ljust(6)
    print("{:<50} {:<20} {:<6} {:<6}".format(dn, description, speed, mtu))
