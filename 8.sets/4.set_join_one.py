names_one = {'anonymous','farha','troy'};
names_two = {'xenon','neon','troy'};

print("names_one : ",names_one);
print("names_two : ",names_two);

# union
print("\n\nAfter union between names_one and names_two : ");
new_names = names_one.union(names_two);
print(new_names);

# update 
# it work like union it that case it update the set
names_one.update(names_two);
print("\nAfter name_one updae : ");
print(names_one);
