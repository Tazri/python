# create two dictionary
person = {
    'Name' : 'Md Tazri',
}

extra_infromation = {
    'Favorite Subject' : 'Science',
    'Height' : '5foot',
}

# print person
print("person : ",person);

# add age in person by list literal :
person['age'] = 17;
print("\n\nAfter add age : ");
print(person);

# update person by extra_information 
person.update(extra_infromation);
print("\n\nAfter person update by extra_information : ");
print(person);