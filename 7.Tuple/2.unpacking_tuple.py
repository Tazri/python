# create packing tuple.
names = ('anonymous','tazri','focasa','troy');

print("names :",names);

# unpacking tuples
(name_one,name_two,name_three,name_four) = names;
# must care tuple item = unpacking item
print("\n\nunpacking names: ");
print("name_one : ",name_one);
print("name_two : ",name_two);
print("name_three : ",name_three);
print("name_four : ",name_four);

# if you can not know how many item packing then use asterist operator
# asterisk* operator
(n_one,n_two,*n_list) = names;
print("\n\n*Asterisk : ");
print("n_one : ",n_one);
print("n_two : ",n_two);
print("n_list : ",n_list);

# we can use asterisk in middle, start and anywhere
(one,*l_list,two) = names;
print("\n\nUsing *Asterisk in middle :")
print("one : ",one);
print("l_list : ",l_list);
print("two : ",two);