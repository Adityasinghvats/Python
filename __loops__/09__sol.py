items = ["apple","banana","orange","apple","mango"]

unique_item = set()
# set only takes unque elements

for item in items:
    if item in unique_item:
        print(item,"is duplicate")
        break
    unique_item.add(item)

            