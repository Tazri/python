# create global variable inside the function
def one():
    global x;
    x = "This is global Variable.";
def two():
    global x;
    x = "This is changing global Variable."

# calling function
one();
print("x : "+x);

# changing global variable by calling function
two();
print("x : "+x);