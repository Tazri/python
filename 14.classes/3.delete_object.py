class Point :
    def __init__(self,_x,_y) :
        self.x = _x;
        self.y = _y;


position = Point(3,2);
print("> position : ",position);
print("> position.x : ",position.x);
print("> position.y : ",position.y);

# delete x property
del position.x;
# print("position.x : ",position.x); this line must throw error

# delete position object
del position;
# print("position : ",position); This line must throw error

# if you create class but do not have content in that case use pas keyword
class Person :
    pass