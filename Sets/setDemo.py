# sets in python typically used for union, intersection, difference, complement ect. 
# set does not have specific order 
# Immutable ( can't update set )

# creating sets
days = {'mon','tue','wed','thur','fri','sat'}
months = {'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'}
Dates = {21,22,23}
print(days)
print(months)
print(Dates)


# accessing values in sets

print("-----days-----")
for d in days:
    print(d)

# adding items to set
days.add('sun')
print(days)


#removing items from set
days.discard('mon')
print(days)


DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])

#union of sets 
# combines both the sets and returns unique records
print("-------- Union Of Sets --------")
AllDays = DaysA|DaysB
print(AllDays)


#Intersection of sets 
# returns only common records
print("-------- Intersection Of Sets --------")
AllDays = DaysA & DaysB
print(AllDays)

#Difference of sets
# returns all elements from 1st set and eliminates 2nd set as well as common items 
print("-------- Difference Of Sets --------")
AllDays = DaysA - DaysB
print(AllDays)


#compare sets
# we can check is set is a subset or superset of another set 

DaysX = set(["Mon","Tue","Wed"])
DaysY = set(['mon','tue','wed','thur','fri','sat','sun'])
# Concept not clear, need to varify again

subsetRes = DaysX <= DaysY
supersetRes = DaysY >= DaysX
print(subsetRes)
print(supersetRes)
