# items = (["fiddleheads", "okra", "kohlrabi"])
items = (["kiwi", "durian", "starfruit","papaya", "pineapple","passion fruit", "banana"])


def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        connect = " and "
        return connect.join(items)
    elif len(items) > 2:
        penult = len(items)-2
        last = len(items)+1
        x = slice(penult,last)
        last_two = items[x]
        comma_list = items[:-2]
        non_oxford = ", "
        connect = ", and "
        list_string = non_oxford.join(comma_list) + ", " + connect.join(last_two)
    return list_string
    
# print(oxford_comma(items))
