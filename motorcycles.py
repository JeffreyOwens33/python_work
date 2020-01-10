motorcycles = ['honda', 'yamaha', 'suzuki']

# changing a name in the list:
# motorcycles[0] = 'ducati'
# print(motorcycles)

# add new element to list:
# motorcycles.append('ducati')
# print(motorcycles)

# add new element to list at any point
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove item from list
#del motorcycles[1]
#print(motorcycles)

#pop lets you work with item after removal from list
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

#print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

#first_owned = motorcycles.pop(0)
#print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#removing item from list
#motorcycles.remove('yamaha')
#print(motorcycles)

#remove a value
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
