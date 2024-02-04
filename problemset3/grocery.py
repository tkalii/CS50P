#Grocery List
grocery = {}
while True:
    try:
        item = input().lower()
        if item in grocery:
            #count the items
            grocery[item] += 1        
        elif item not in grocery:
            grocery[item] = 1
    except EOFError:
        #loop and sort to print
        for key in sorted(grocery.key()):
            #add the number of items to prefix
            print(grocery[key], key.upper())
        break

