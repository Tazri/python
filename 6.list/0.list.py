list_number = [23,32,3,2,1];

print("list_number : ",list_number);

# create list by list constructor
fruits = list(('Apple','Benana','Orange','Mango'));
print("fruits : ",fruits);

print('len(list_number) : ',len(list_number));

print("fruits[0] : ",fruits[0]);
print("fruits[-1] : ",fruits[-1]);

# we can apply range like string
print("fruits[1:] : ",fruits[1:]);
print("fruits[1:3] : ",fruits[1:3]);
print("fruits[1:-1] : ",fruits[1:-1]);

# change list item
fruits[0] = "Red Mango";
print("fruits : ",fruits);

# change range items
fruits[1:3] = ['Black Apple',"Red Apple"];
print("after change range furits : ",fruits);