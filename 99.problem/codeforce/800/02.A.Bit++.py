n = int(input());

x = 0;

for i in range(n):
    op = input();

    if op in ["X++","++X"]:
        x += 1;
    elif op in ["X--","--X"]:
        x -= 1;

print(x);