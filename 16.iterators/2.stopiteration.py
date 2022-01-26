# create class
class My_Range : 
    def __init__(self,_start,_end,_increament = 1) :
        self.start = _start;
        self.end = _end;
        self.increament = _increament;

    def __iter__(self) :
        return self;

    def __next__(self) :
        if self.start < self.end :
            x = self.start;
            self.start += self.increament;
            return x;
        else :
            raise StopIteration;

# create my range
my_range = My_Range(1,5);
my_iterator = iter(my_range);

print("myrange : ",my_range);
print("my_iterator : ",my_iterator);

print("\n\n>>> See value by next <<<");
print("next(my_iterator) : ",next(my_iterator));
print("next(my_iterator) : ",next(my_iterator));
print("next(my_iterator) : ",next(my_iterator));
print("next(my_iterator) : ",next(my_iterator));

# it's throw a error because limit is finish
# print("next(my_iterator) : ",next(my_iterator));