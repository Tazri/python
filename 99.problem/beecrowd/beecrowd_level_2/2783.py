space,stamp_number,exist_number = [int(i) for i in input().split()];

# get stamps
stamps = [i for i in input().split()];

# album
album = [i for i in input().split()];

total_found = stamp_number;
for stamp in stamps :
    if stamp in album:
        total_found -= 1;

print(total_found);