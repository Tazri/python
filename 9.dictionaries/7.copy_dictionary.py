# create simple dictionary
person_one = {
    'name': 'tazri',
    'age' : 17
}

# direct method
person_two = person_one;

print("person_one : ",person_one);
print("person_two : ",person_two);

# changing value in person two and see what happen
person_two['name'] = 'focasa';

print("\n\nAfter change name in person two : ")
print("person_one : ", person_one);

# in that case here it copy just reference not dictionary

# fix it again
person_one['name'] = 'tazri'

# use copy method
copy_person = person_one.copy();
copy_person['name'] = 'solus';
print("\n\nchanging copy person value and seee : ");
print("person_one : ",person_one);
print("copy_person : ",copy_person);

# copy by dict constructor
dict_person = dict(person_one);
dict_person['name'] = 'xenon';
print("\n\ncopy the person_one by dict constructor and change name value of dict_person and see : ");
print("person_one : ",person_one);
print("dict_perosn : ",dict_person);