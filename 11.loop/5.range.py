# let's see range
from lib2to3.pgen2.literals import simple_escapes


simple_range = range(5);
print("simple_range : ",simple_range);

# print 1 to 5
print(">>> 1 TO 5 <<<");
for i in simple_range : 
    print("> ",i);

# print 10 to 15
print("\n\n>>> 10 TO 15 <<<");
for i in range(10,15) :
    print("> ",i);

# print even number from 20 to 30
print("\n\n>>> EVEN 20 TO 30 <<<");
for i in range(20,30,2) :
    print("> ",i);