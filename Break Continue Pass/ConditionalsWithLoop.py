# Break : used to break the program execution at specific condition
# the break statement provides you with the opportunity to exit out of a loop when an external condition is triggered.
# Continue : to skip particular condition
# pass : there is probability that in future specific condition will be true


print("------- Use of break statement ---- ")
number = 0
print(type(number))
for i in range(10):
    number += 1
    if number == 5:
        break
    print('number is ' + str(number))
print("out of the loop") 

print("------- Use of continue statement ---- ")
number = 0
print(type(number))
for i in range(10):
    number += 1
    if number == 5:
        continue
    print('number is ' + str(number))
print("out of the loop") 

print("------- Use of pass statement ---- ")
number = 0
print(type(number))
for i in range(10):
    number += 1
    if number == 5:
        pass
    print('number is ' + str(number))
print("out of the loop") 