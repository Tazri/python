def decode(s) : 
  map = {};
  chip = "";

  for char in s:
    if  not map.get(char) : 
      chip += char;
      map[char] = True;

  chip = list(chip)
  chip.sort();
  chip = "".join(chip);
  
  
  # made the map
  for i in range(len(chip)):
    map[chip[i]] = chip[-(i+1)];

  # now build the main string
  message = "";

  for char in s:
    message += map[char];

  return message;

total_case = int(input());

for i in range(total_case):
  input();
  print(decode(input()))