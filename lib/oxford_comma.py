# items = (["fiddleheads", "okra", "kohlrabi"])
items = (["kiwi", "durian", "starfruit"])


def oxford_comma(items):
    if len(items) == 1:
        # for item in items:
        return items[0]
    elif len(items) == 2:
        connect = " and "
        return connect.join(items)
    elif len(items) > 2:
        (-2:-1)

    
print(oxford_comma(items))
