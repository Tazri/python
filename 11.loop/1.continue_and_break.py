# Example of continue and break keyword

# continue
i = 1;

print(">>> Even Under 0 to 20 <<<");
while i < 20 : 
    if i & 1 : 
        i += 1;
        continue;
    
    print("> Even : ",i);
    i += 1;

i = 1

# break
print("\n>>> Try Print 1 to 10 <<<");
while True :
    if i == 5 : break; 
    print("> I : ",i);
    i += 1;