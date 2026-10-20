my_dict = {
    "name" : "Hassan",
    "age" : 30,
    "age" : 31,    
}

print(my_dict)
print(type(my_dict))
print(len(my_dict))

print(my_dict["name"])
print(my_dict["age"])

new_dict = {
    "name" : "Hassan",
    "age" : 30,
    "age" : 31,
    "color" : ['Red', 'Green', 'Yellow']    
}

print(new_dict)

my_dict["name"] = "Ali"
print(my_dict)
my_dict.update({
    "name" : "Hassan",
    "age" : 30,
    "city" : "Beirut",  
})
print(my_dict)
my_dict.update({"city" : "Tyre"})
print(my_dict)

my_dict["city"] = "Bintjbeil"
print(my_dict)

my_dict["country"] = "Lebanon"
print(my_dict)

my_dict.pop("age")
print(my_dict)

del my_dict["city"]
print(my_dict)

my_dict.clear()
print(my_dict)
