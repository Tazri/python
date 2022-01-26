# create basic iterator
names = ['anonymous','focasa','solus','tazri','troy','pendora','parrot'];
names_iterator = iter(names);

print("names : ");
print(names);

print("\n\n>>> Let's see value by next function <<<");
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));
print("next(names_iterator) : ",next(names_iterator));

# it throw error because iterator is finish
# print("next(names_iterator) : ",next(names_iterator));

# it throw error because number is not iterable object
# number = iter(332);

# create iterator by range
range_iterator = iter(range(0,6,2));
print("\n\n>>> Let's see range iterator <<<");
print("> next(range_iterator) : ",next(range_iterator));
print("> next(range_iterator) : ",next(range_iterator));
print("> next(range_iterator) : ",next(range_iterator));