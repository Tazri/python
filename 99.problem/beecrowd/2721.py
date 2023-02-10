reindeers = ["Dasher", "Dancer", "Prancer", 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph'];

numbers = [int(i) for i in input().split()];
sums = sum(numbers);
index = sums%9;

if index == 0:
    index = 8;
else:
    index = index - 1;

print(reindeers[index]);