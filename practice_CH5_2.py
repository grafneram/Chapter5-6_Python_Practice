

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")  # Print item count and name
        item_total += count  # Add to total count
    print("Total number of items:", item_total)


def addToInventory(inventory, addedItems):
    for item in addedItems: #Adds items to inventory dict
        inventory[item] = inventory.get(item, 0) + 1  # Increment count or set to 1 if new
    return inventory


# ex data given in the example:
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot) # Update inventory with dragon loot
displayInventory(inv) #display current inventory
