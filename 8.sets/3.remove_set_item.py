names = {'anonymous','tazri','focasa','troy','farha'};

print("names : ",names);

# remove 'anonymous'
names.remove('anonymous');
print('after remove anonymous then : ');
print(names);

# we can not remove item which can not exist in set 
# names.remove('anonymous'); it must throw error


# discard is another methods to remove item
names.discard('tazri');
print("\n\nremove tazri with discard then : ");
print(names);

# we can remove item which can not exist in set with discard
# in that case it can not throw error
names.discard('tazri');

# pop 
# pop remove last element but we know that set is not ordered
# in that case it remove randomly one item from set
print("\n\n after names.pop() : ");
names.pop();
print(names);

# clear 
# remove all item from sets
names.clear();
print("\nafter names.clear() : ");
print(names);

# del
# delete the set
del names;
# print("\nafter del names : ");
# print(names);
# must be throw a error here