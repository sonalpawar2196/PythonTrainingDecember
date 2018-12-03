# creating and displaying dictionary 
cars = {
    "name" : "BMW",
    "model" : "X5",
    "color" : "Neavy Blue"
}

print(cars)

# accessing dictionary items by referring key name and square brackets 
print("car model : "+cars["model"])

# for accssing dictionary items "get" also gives same result

x = cars.get("model")
print("accessing via get function  car model  : " + x)

# You can change the value of a specific item by referring to its key name
# model changed from x5 to x6
# error occure when tried to do [print("cars :"+cars)] error: must be str , not dict
cars["model"] = "X6"
print(cars)

#Loop Through a Dictionary

# Print all keys in the dictionary, one by one:
print("accessing all keys of dictionary ")
for x in cars: 
    print(x)
    
# Print all values in the dictionary, one by one:
print("accessing all values of dictionary ")
for x in cars: 
    print(cars[x])

# there is also values() function for accessing only values 
print("accessing all values of dictionary through values() function ")
for y in cars.values():
    print(y)

# loop through both key and values through items() function
print("accessing keys and values through items() function")
for x,y in cars.items():
    print(x,y)

    
# Check if Key Exists
if "model" in cars:
    print("yes, model key exist in cars dictionary")
    
    
# To determine how many items (key-value pairs) a dictionary have, use the len() method.
print(len(cars))


# -------------  adding items in dictionary ----------------
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
cars["price"] = "60L"
print(cars)

# -------------  removing items from dictionary ----------------
# The pop() method removes the item with the specified key name:

cars.pop("price")
print(cars)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
cars.popitem()
print(cars)

# The del keyword removes the item with the specified key name:
del cars["model"]
print(cars)

# The del keyword can also delete the dictionary completely:
#del cars
# after deleting dictionary cars it throws error coz dictionary is no longer exist 
# error : name 'cars' is not defined
# print(cars)

# Clear() keyword empties entire dictionary
cars.clear()
print(cars)


# copy() function copies one dictinary into another
bikes = {
    "name" : "duke",
    "color" : "black",
    "price" : "1.2L"
}

x = bikes.copy()
print(x)


# fromkeys()  Returns a dictionary with the specified keys and values
keys = {'a','e','i','o','u'}
values = 'vowel'
vowels = dict.fromkeys(keys,values)

print(vowels)
