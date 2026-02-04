#task 1

inventory = ["Bananas","Apples", "Dates", "Carrots"]
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print(inventory)

#task 2

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temperatures[0], temperatures[-1])
print(temperatures [3:6])
print(temperatures [-3:])


#task 3

screen_res = (1920, 1080)
print(f"Current Screen Resolution: {screen_res[0]}x{screen_res[1]}")
#screen_res[0] = (1280) 
print("Tuples cannot be modified!")