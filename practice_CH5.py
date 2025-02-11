# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")  # Print item count and name
        item_total += count  # Add to total count
    print("Total number of items:", item_total)

displayInventory(stuff)
