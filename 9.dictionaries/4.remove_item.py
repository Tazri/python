# create dictionary 
person = {
    'name' : 'Tazri',
    'age' : 17
}

person['favorite subject'] = 'Science';
person['height'] = '5.1foot';
person['weight'] = '45kg';

# print person
print("person : ",person);


# use pop to delete weight key
person.pop('height');
print("\n\nafter pop height : ");
print(person);

# we can not delete not exist key by pop
# person.pop('none');
# it must throw error

# popitem
# it remove last item of dictionary but before version 3.7 it remove radomly remove anyone key.
person.popitem();
print("\n\nAfter person.popitem() : ");
print(person);

# del 
# this keyword can use delete key from object
del person['age'];
print("\nAfter del person['age'] : ");
print(person);

# we can not delete key which is not exist in dicitionary

# clear 
# this method use here to clear the all dictionary easily
person.clear();
print("\n\nAfter person.clear() : ");
print(person);