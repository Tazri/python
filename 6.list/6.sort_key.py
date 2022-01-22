# customize sort key
name_list = ['Tarri','focasa','anonymous','Droy','Farha','solus'];
number_list = [3,342,2,232,321,32,4,234];

print("name_list : ");
print(name_list);

# sort this name list case insensitive way
name_list.sort(key = str.lower);
print("\n\nname_list.sort(key = str.lower)");
print(name_list);

## create own key
def our_key (x) :
    return x + 30;

print("\n\nnumber_list : ");
print(number_list);

number_list.sort(key = our_key);
print("\n\nnumber_list.sort(key = our_key) : ");
print(number_list);

# we can use reverse methods to reverse the list
name_list.reverse();
print("\n\nname_list.reverse() : ");
print(name_list);
