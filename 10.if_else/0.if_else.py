# create basic if elif
a = 29;
b = 32;
c = 321;

# see how else if work in python
if a > b and a > c :
    print("a is greatest value.");
elif b > a and b > c :
    print("b is greatest value.");
else : 
    print("c is greatest value.");

# if need to empty if statement of something like that then use pass keyword
if 3 :
    pass;

# we can use if and elif keyword like ternary operator.
print("a is greatest value.") if a > b and a > c else print("c or b greatest value");

# one line if elif
if a > b : print("\n\na is greater than b.");
else : print("\n\nb is greater than a.");