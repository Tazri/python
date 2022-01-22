# create sets
names = {'anonymous','tazri','farha'};
extra_name = {'tazri','farha','troy'};
name_list = {'solus','xenon','neon'};
name_tuple = ('helium','hydrogen');

print("names : ",names);

# add focasa in names
print("add 'focasa' than set : ");
names.add("focasa");
print(names);

# update method
print("\n\nadd extra_name in set with update method : ");
names.update(extra_name);
print(names);

# update set with list
print("\nadd name_list in set with update method : ");
names.update(name_list);
print(names);

# update set with tuple
print("\nadd name_tuple in set with update method : ");
names.update(name_tuple);
print(names);
