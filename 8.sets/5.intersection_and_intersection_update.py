names_one = {'anonymous','farha','troy','tazri'};
names_two = {'tazri','solus','xenon','anonymous','focasa'};

print("names one : ",names_one);
print("names two : ",names_two);

# intersection 
new_names = names_one.intersection(names_two);
print("\n\nnames_one and names_two intersection and create new_names : ");
print("new_names : ",new_names);

# intersection_update
# it can not return new set just update the set
names_one.intersection_update(names_two);
print("\n\nnames_one intersection update with names_two : ");
print("names_one : ",names_one);