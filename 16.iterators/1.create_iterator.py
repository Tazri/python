# create iterator
class Number_Iterator : 
    def __init__(self,_x,_increament) :
        self.x = _x;
        self.increament = _increament;
    def __iter__(self) :
        return self;
    def __next__(self) :
        x = self.x;
        self.x += self.increament;
        return x;

# create iterator by number iterator
iterable_object = Number_Iterator(10,5);

# see the iterable object
print("iteratble_object : ");
print(iterable_object);

# create iterator
my_iterator = iter(iterable_object);

print("\nmy_iterator : ");
print(my_iterator);

# see value by next
print("\n\n>>> See value by next <<<");
print("> next(my_iterator) : ",next(my_iterator));
print("> next(my_iterator) : ",next(my_iterator));
print("> next(my_iterator) : ",next(my_iterator));
print("> next(my_iterator) : ",next(my_iterator));