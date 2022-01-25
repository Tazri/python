# create small mini lambda
sum = lambda a,b : a+b;
multiply = lambda a,b : a*b;

print(">>> sum(3,5) : ",sum(3,5));
print(">>> multiply(5,3) : ",multiply(5,3));

# create function which get lambda function as peramter
def operation(a,b,l) :
    return l(a,b);

print("\n\n>>> operation(3,2,sum) : ",operation(3,2,sum));
print("\n\n>>> operation(4,3,multiply) : ",operation(4,3,multiply));

# create funciton which return lambda
def return_lambda(n) :
    return lambda a : n*a;

m_5 = return_lambda(5);

print("\n\n>>> m_5(5) : ",m_5(5));