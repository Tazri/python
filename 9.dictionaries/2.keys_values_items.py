person = {
    "name" : "Tazri",
    "age" : 17
}

print("person : ");
print(person);

# keys method
print("\nperson.keys() : ",person.keys());
# value method 
print("person.values() : ",person.values());
# items method
print("person.items() : ",person.items());

## update dictionary
person['height'] = '5inh'
print("\n\n>>> After Update Dictionary <<<");
print("\nperson.keys() : ",person.keys());
# value method 
print("person.values() : ",person.values());
# items method
print("person.items() : ",person.items());

## we can check key is exist in dictionary or not with membership operator
print("\n'name' in perosn : ",'name' in person);
print("\n'name' not in person : ",'name' not in person);