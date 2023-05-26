import math

def get_point(n):
    if(n == 1):
        return (1,1);
    
    # get row number 
    sqrt_n = math.sqrt(n);
    row_no = math.ceil(sqrt_n);
    prev_row = row_no - 1;
    is_even_row = False if row_no & 1 else True;

    # get start and end
    start = (prev_row**2)+1;
    end = row_no**2;
    mid = int((start+end) /2);
    mid_index = row_no;

    # if mid == n then mid_index is point
    if mid ==  n:
        return (mid_index,mid_index);

    diff = mid - n;
    diff = diff if diff > 0 else -1*diff;
    
    # first figure out the point for even number
    if(is_even_row):
        x = mid_index - diff;
        y = mid_index;

        # n is lower 
        if n < mid:
            return (x,y);
        else: 
            return (y,x);
    
    # figure out for odd row
    x = mid_index - diff;
    y = mid_index;


    if(n > mid):
        return (x,y);
    else:
        return (y,x);

def print_point(i,x,y):
    print("Case "+str(i)+": "+str(x)+" "+str(y));

# solve the real problem
total_test = int(input());

for test in range(1,total_test+1):
    n = int(input());

    x,y = get_point(n);
    
    print_point(test,x,y);