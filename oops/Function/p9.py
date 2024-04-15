def find_largest_item(lst):
    if not lst: 
        return "List is empty"
    else:
        max_item = max(lst)
        return max_item

x = [4, 6, 8, 24, 12, 2]
largest_item = find_largest_item(x)
print("The largest item in the list is:", largest_item)
