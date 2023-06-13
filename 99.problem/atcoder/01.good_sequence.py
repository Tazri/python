# problem link : https://atcoder.jp/contests/arc087/tasks/arc087_a
# problem name : Good Sequence
# judge name : atcoder
# language version : Python 3.9.2
# status : accepted

size = int(input());
sequence = [int(str_int) for str_int in input().split()];
map = {};
remove_times = 0;

for number in sequence :
    if(not map.get(number)):
        map[number] = 1;
    else:
        has = map[number];

        if(has >= number):
            remove_times += 1;
        else:
            map[number] += 1;

# remove which are not profer time in map
for number in sequence:
    has = map[number];

    if not has : continue;

    if has < number :
        remove_times += has;
        map[number] = 0;

print(remove_times);