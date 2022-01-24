# recursion
def fact(n) :
    if n <= 0 : 
        return 1;
    else :
        return n * fact(n - 1);

print(">>> fact(2) : ",fact(2));
print(">>> fact(3) : ",fact(3));
print(">>> fact(4) : ",fact(4));
print(">>> fact(5) : ",fact(5));