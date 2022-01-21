sentence = "my name is Md Tazri and I am Student.Do you know me ? i want to be a programmer.";

print("sentence : ");
print(sentence);

# make capital first letter
print("\n\nsentence.capitalize()");
print(sentence.capitalize());

# make string upper
print("\n\nsentence.upper()");
print(sentence.upper());

# make string lower case
print("\n\nsentence.lower()");
print(sentence.lower());

# make string title
print("\n\nsentence.title() : ");
print(sentence.title());

# make string lowercase by casefold
print("\n\nsentence.casefold() : ");
print(sentence.casefold());

# count i how many time 
print("\n\nsentence.count('i') : ");
print(sentence.count('i'));

# count 'name' string position 0 to 8
print("\n\nsentence.count('name',0,8)");
print(sentence.count('name',0,8)); ## by default start is 0 and end is -1

# find 'tazri' in string 
print("\n\nsentence.find('tazri') : ");
print(sentence.find('tazri'));

# find 'Tazri' in string 
print("\n\nsentence.find('Tazri') : ");
print(sentence.find('Tazri'));

# saytax of find is :
# find(value,start_index,end_index);
# by default start = 0 and end is -1
# it return start position of sub_string in string
# if return -1 if sub_string not exist in string
