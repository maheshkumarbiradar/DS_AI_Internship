#tas1

contact = {"abc": 98764, "efg": 36458, "xyz": 43557}
contact["mno"]= 23734

for name,num in contact.items():
    print(name,num)
    
print("\n\n",contact.get("mno"))

#task 2

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print (unique_users)
print("ID05" in unique_users)
print("ID10" in unique_users)
print(len(unique_users))

#task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_a | friend_b)
print(friend_a & friend_b)
print(friend_a - friend_b)