def countPair(arr):
  total = 0;
  for i in range(len(arr)-3):
    b1, b2 , b3 = arr[i],arr[i+1],arr[i+2];
    
    for j in range(i+1,len(arr)-2):
      c1,c2,c3 = arr[j],arr[j+1],arr[j+2];
      
      con1 = b1 != c1 and b2 == c2 and b3 == c3
      con2 = b1 == c1 and b2 != c2 and b3 == c3
      con3 = b1 == c1 and b2 == c2 and b3 != c3
      
      if con1 or con2 or con3 :
        total += 1;

  return total;

      

cases = int(input());

for i in range(cases):
  input();
  arr = [int(x) for x in input().split()];

  totalPair = countPair(arr);

  print(totalPair);


