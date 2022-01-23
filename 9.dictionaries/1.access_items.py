# create simple dictionary
person = {
    'name' : "Md Tazri"
}

print("person : ",person);

# access with list literal
print("\nperson['name'] : ",person['name']);

# access with get method 
print("\nperson.get('name') : ",person.get('name'));

# if we can create key by list literal
person['age'] = 17;
print("\nafter create key value then : ");
print(person);


# try to access not exist key by list literal
# print("\nperson['n'] : ",person['n']);
# it must be throw error

# try to access not exist key by get
print("\nperson.get('n') : ",person.get('n'));
# it reaturn none