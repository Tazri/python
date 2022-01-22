# create list with lietral
list_number = [3,2,2,3];

# create list with constructor
name_list = list(("Tazri","Focasa","Troy","Farha"));
name_unkown = ['Anonymous',"Polymorphisom"];
fruits = ['apple','apple','mango','orange','benana'];

# Read : print list
print(list_number);

# update list by methods

# insert
print("name_list : ",name_list);
print("After Update >>> ");
name_list.insert(1,"Solus");
print(name_list);

# append 
name_list.append("Droy");
print("name_list : ",name_list);

# extend
name_list.extend(name_unkown);
print("name_list : ",name_list);

# Delete by methods
print("fruits : ",fruits);

# remove
print("furits remove apple : ");
fruits.remove("apple");
print(fruits);

# pop 
# remove last item if can not give index
print("fruits after pop and pop(0) : ");
fruits.pop();
fruits.pop(0);
print(fruits);
