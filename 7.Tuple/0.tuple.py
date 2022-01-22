# create tuple
fruits = ("apple","benana","mango","apple","mango");

print("fruits : ");
print(fruits);
print("type(fruits) : ");
print(type(fruits));

# access single value like list
print("fruits[2] : ",fruits[2]);
print("fruits[-1] : ",fruits[-1]);

# try to know tuple length like list
print("\n\nlen(fruits) : ",len(fruits));

# if try to create single item tuple must be care about coma first
no_coma_tuple = ('apple');
print("\n\nno_coma_tuple : ",no_coma_tuple);
coma_tuple = ('apple',);
print("coma_tuple : ",coma_tuple);

# can you create tuple by tuple construction
names = tuple(('Anonymous','Tazri','Troy','Farha','Focasa'));
print("\n\nnames : ",names);

# we can not change tuple