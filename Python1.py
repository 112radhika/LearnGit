print("Hello")
b = 9
c="test"
d=9.8
# using comma
print("The value of b is", b)
# using fstring
print(f"value of b is {b}")
# one way of concatenating two data types
print("{} {}".format("The value of the variable b is", b))
# to get the type of variable
print(type(b))
print(type(c))
print(type(d))

# List operations
# List operations

names = ['dev', 'devootan', 'devansh']
print(names[0]) # dev
print(names[-1])  # to get the last item in the list use -1 =>devansh

names.insert(2,"kunjikka")  # to insert a value into
# the list at any position =>['dev', 'devootan', 'kunjikka', 'devansh']
print(names)

names.append("shumbudu")  # add new value at the end =>['dev', 'devootan', 'kunjikka', 'devansh', 'shumbudu']
print(names)

print(names[1:4])  # to get the sublist/slice from a list where
# 1st index is inclusive and 4th index is exclusive =>['devootan', 'kunjikka', 'devansh']

names[3] = "DEVANSH"  # to update the value in a list=> ['dev', 'devootan', 'kunjikka', 'DEVANSH', 'shumbudu']
print(names)

del names[0]  # to delete value from the index =>['devootan', 'kunjikka', 'DEVANSH', 'shumbudu']
print(names)

names.pop(0)  # to remove an element by index =>['kunjikka', 'DEVANSH', 'shumbudu']
print(names)

names.remove("shumbudu") # Removes the first occurrence of the value => ['kunjikka', 'DEVANSH']
print(names)

print(names.index("DEVANSH"))
print("DEVANSH" in names)  # in is used to check if an item exist in the list => true
print("shumbudu" in names)  # false

names.append("kunju")
names.sort()  # sort the list in ascending order
print(names)

names.reverse()  # reverse the items in the list
print(names)

print(len(names))  #to get the length of the list

copied_names = names.copy()  # to copy the list
print(copied_names)

names = ['kunju', 'kunjikka', 'DEVANSH', 'kunju']
print(names.count('kunju'))  # count the number of occurrence of the value

# Tuple - immutable.del, insert, append, update operations are not possible
place = ('kappil', 'kudassanad','bangalore')
print(place[0])
print(place[-1])

# Dictionary
car = {1:2, "first":"taigun", "ok":2, 3:"lets see"}
print(car)
print(car["ok"])
print(car[3])

# empty dictionary and enter values to it
val = {}
val[1] = "first"
val["second"] = 2
val["third"] = "three"
val[4]=4
print(val)



