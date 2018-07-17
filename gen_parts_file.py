import json

parts = json.loads(open("parts.json", "r").read())
del parts["Initiator"], parts["Owner"], parts["StorageClass"]
for x in parts["Parts"]:
    x.pop("LastModified", None)
    x.pop("Size", None)

json.dump(parts, open("parts_processed.json", "w"))
