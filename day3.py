# 5 stars
def organizeInventory(inventory):
    inventory_ordered = {}

    for value in inventory:
        if value["category"] not in inventory_ordered:
            inventory_ordered[value["category"]] = {}

        if value["name"] not in inventory_ordered[value["category"]]:
            inventory_ordered[value["category"]][value["name"]] = value["quantity"]
        else:
            inventory_ordered[value["category"]][value["name"]] += value["quantity"]

    return inventory_ordered
