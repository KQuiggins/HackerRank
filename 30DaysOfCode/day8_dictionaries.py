""" Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.  """

n = int(input())

phoneBook = {}


entries = [input().split() for _ in range(n)]
    
phoneBook = {k:v for (k,v) in entries}

while True:
    try:
        name = input()
        if name in phoneBook:
            print(f"{name}={phoneBook[name]}")
        else:
            print('Not found')
    except:
        break


print(entries)
print(phoneBook)
