# create simple class which name is Point
from operator import pos


class Point : 
    x = 40;
    y = 43;

# create Point object
position = Point();

print(">>> Position <<<");
print("position.x : ",position.x);
print("position.y : ",position.y);

# changing position property
position.x = 0;
position.y = 0;

print("\n\n>>> After Change Position Properties <<<");
print("position.x : ",position.x);
print("position.y : ",position.y);
