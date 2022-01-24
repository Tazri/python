# aribitrary keyword arguments

def just_see(**dictionary) :
    print("dictionary : ");
    print(dictionary);

print(">>> just_see(name='tazri',age=17) : ");
just_see(name='tazri',age=17)

print("\n>>> just_see() : ");
just_see();

# below this code will throw error
# print("\n>>> just_see(32) : ");
# just_see(32);
