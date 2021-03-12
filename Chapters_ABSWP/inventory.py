import pprint


stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger' :1, 'arrow' :12 }


def displayinventory(inventory):
    print("Inventory : ")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print((k.ljust(10) + ':  ' + str(v).rjust(10)))
    print(pprint.pformat("total number item : " + str(item_total)))
    return item_total

def addToInventory(inventory, addedItems):
    add_item = inventory.copy()
    for k in addedItems:
        add_item[k] = add_item.get(k,0)+1
    return add_item


displayinventory(stuff)

inv = { 'gold coin': 42, 'rope':1}
dragonLoot = [ 'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayinventory(inv)
