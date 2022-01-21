sentence = "My name is md Tazri and I am a simple students nothing else.";
tuple = ('black','yellow','red','dry');


print("sentence : ");
print(sentence);

# replase
'''
replace sayntax
string.replace(value,new_value,count)

by default it replace all old value by new value other wish it replace count time.
'''

print("\n\nsentence.replace('s','t') : ");
print(sentence.replace('s','t'));

print("\n\nsentence.replace('m','l',2) : ");
print(sentence.replace('m','l',2));

# swapcase() 
# swapcase return the string where all letter swap from upper to lower and lower to upper.

print("\n\nsentence.swapcase() : ");
print(sentence.swapcase());

# join()
# take iterable object and it join them as string by some thing
# syntax
# value.join(tuple)
# it joint by value every element of iterable object

print("\n\ntuple : ");
print(tuple);
print("\n\n''.join(tuple) : ");
print(''.join(tuple));

print("\n\n'--> '.join(tuple) :");
print('--> '.join(tuple));
