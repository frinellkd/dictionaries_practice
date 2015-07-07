filename = open("scores.txt")

restaurants = {}
restaurant_list = []

for line in filename:
    stripped_name = line.rstrip()
    name = stripped_name.split(":")

    restaurant_list.append(name)
    


for item in restaurant_list:
    key = item[0]
    value = int(item[1])
    restaurants[key] = value


keys_in_dict = sorted(restaurants)


for restaurant_name in keys_in_dict:
    print "%s is rated at %d" % (restaurant_name, restaurants[restaurant_name])
    