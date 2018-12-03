
thisList =  ['sonal','priya','abc','pqr']
print(thisList)
print(thisList[1])
thisList[1] = "jjj"
print(thisList)
# iterating over list
for x in thisList:
    print(x)
if "sonal" in thisList:
    print("string  is in the list")
else:
    print("not present ")
    
print("length of list = ",len(thisList))

#To add an item to the end of the list, use the append() method:
thisList.append("pooja")
print(thisList)

#To add an item at the specified index, use the insert() method:
thisList.insert(1,"one")
print(thisList)
print("length of list = ",len(thisList))

#There are several methods to remove items from a list:
# remove, pop, clear, del

#The remove() method removes the specified item:
thisList.remove("pooja")
print("1 item removed from list")

#The pop() method removes the specified index, (or the last item if index is not specified):
thisList.pop(3)
print(thisList)

#The del keyword removes the specified index:
del thisList[0]
print(thisList)
# ------------------------------------------------------------------
# clear() make entire list empty 
thisList[:]
print(thisList)

# coping one list to another

fruites = ["apple","banana","grapes","orange","apple"]
x = fruites
print(x)

#---------------------------------------------------------------------

# count() function returns how many times perticular item occure in the list
countAPPLE = fruites.count("apple")
print(countAPPLE)

# extend() used when you want to add element at the end of current list
cars = ["BMW","AUDI","MERCEDIES","JAGUAR"]
fruites.extend(cars)
print(fruites)

# index() : returns the index of perticular item 
y = fruites.index("BMW")
print(y)
