# example of for loop on list, string
name_list = ['anonymous','solus','focasa'];
my_name = "MD Tazri";

# for loop on name_list
print(">>> Name List <<<");
for name in name_list :
    print("> ",name);

# for loop on my_name
print("\n\n>>> Letter in My Name <<<");
for letter in my_name :
    if letter == ' ' : continue;
    print("> ",letter);

# for loop without content in that case use pass keyword and leave it
for letter in my_name :
    pass;