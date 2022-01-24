# basic function
def sample_function(key_one,key_two) :
    print("> key_one :",key_one);
    print("> key_two :",key_two);

# call function by key
print(">>> Call Sample Function by Key <<<")
what_return = sample_function(key_two=2,key_one=1);

print("\n\nwaht_return : ",what_return);

# if function expect 3 two arguments than must sent two argument. not less or more.

# see *list peramter in funciton
def print_all(*perameter_list) :
    print("peramter_list : ",perameter_list);

print("\n\n>>> print_all('a','b','c') <<<");
print_all('a','b','c');

print("\n\n>>> print_all() <<<");
print_all();

# the list is tuple you can not change it
def print_all(*peramter_list) :
    print("perameter_list[0] : ",peramter_list[0]);
    ## peramter_list[0] = '3'; error here
    print("peramter_list : ",peramter_list);

print("\n\nprint_all('a','b','c') : ");
print_all('a','b','c');