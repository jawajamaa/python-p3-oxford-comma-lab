items = (["kiwi", "durian", "starfruit","papaya", "pineapple","passion fruit", "banana"])

# my solution that works and passes tests 

# def oxford_comma(items):
#     if len(items) == 1:
#         return items[0]
#     elif len(items) == 2:
#         connect = " and "
#         return connect.join(items)
#     elif len(items) > 2:
#         penult = len(items)-2
#         last = len(items)+1
#         x = slice(penult,last)
#         last_two = items[x]
#         comma_list = items[:-2]
#         non_oxford = ", "
#         connect = ", and "
#         list_string = non_oxford.join(comma_list) + ", " + connect.join(last_two)
#     return list_string
    

# Chat GPT's more 'Pythonic' code

def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        comma_list = ", ".join(items[:-1])
        return f"{comma_list}, and {items[-1]}"

print(oxford_comma(items))
