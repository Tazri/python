n = int(input());

total = 0;

for i in range(n):
    if (sum([int(x) for x in input().split(" ")]) >= 2):
        total+= 1

print(total);