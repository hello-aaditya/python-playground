items = ["apple", "banana", "apple", "orange", "mango"]

unique_item = set()

for itr in items:
    if(items.count(itr) > 1):
        print(itr)
        break