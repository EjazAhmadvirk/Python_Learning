Marks = {"English": 95, "Math": 90, "Science": 92}
print(Marks)

print(len(Marks))


Marks.update({"Social": 98})
print(Marks)

print(Marks.values()) # print the values of the dictionary

print(Marks.keys()) # print the keys of the dictionary
print(Marks.items()) # print the items of the dictionary

print(len(Marks))


print(Marks.get("English")) # get the value of the key "English"

Marks.pop("Math") # remove the key "Math" from the dictionary
print(Marks)

Marks.popitem() # remove the last item from the dictionary
print(Marks)


print(type(Marks))

Marks.clear() # clear the dictionary
print(Marks)

Marks.copy() # copy the dictionary
print(Marks)

# Marks.fromkeys() # create a new dictionary with the keys from the list
# print(Marks)
