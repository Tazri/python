names_one = {'anonymous','troy','farha','focasa','tazri','solus'};
names_two = {'troy','solus','focasa','xenon','anonymous'};

print("names_one : ",names_one);
print("names_two : ",names_two);

# symmetric_difference
# return new set where keep all item just not include duplicates
new_names = names_one.symmetric_difference(names_two);
print("\n\nnames_one and names_two symmetric and create new names : ");
print(new_names);

# symmetric_difference_update
# it work like symmetric_difference just it can not return new set and update current set
names_one.symmetric_difference_update(names_two);
print("\n\nnames_one symmetric_difference with name_two : ");
print(names_one);