import math

items = [x for x in range(0, 97)]
  
length_items = len(items)

items_per_page = 5
actual_page = 1

quantity_pages = math.ceil(length_items / items_per_page)

offset = actual_page * items_per_page 

current_data = items[offset - items_per_page:offset]

print(current_data, actual_page)
