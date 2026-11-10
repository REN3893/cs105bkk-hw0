"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory."""
    li = inventory.copy()
    if item in li.keys():
        li[item]+=count
    else:
        li[item] = count
    return li
        
    raise NotImplementedError("core: return a new inventory with the item added")


def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    count = 0
    for inventory in inventories:
        count += sum(inventory.values())
    return count
    raise NotImplementedError("core: add up the items in every inventory")


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    li = []
    for i in inventory.keys():
        if inventory[i] < limit:
            li.append(i)
    li.sort()
    return li
    raise NotImplementedError("core: list the items running low")
