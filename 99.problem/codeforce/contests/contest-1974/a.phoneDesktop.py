import math

def needScreen(x_app,y_app):
  # total screen or y application 
  total_screen = math.ceil(y_app/2);

  # calculate empty cell
  total_cell = total_screen * 15;

  empty_cell = total_cell - (y_app*4) - x_app;

  if empty_cell >= 0 : 
    return total_screen;

  need_cell = -1*empty_cell;

  total_screen += math.ceil(need_cell/15)
  return total_screen;

testCase = int(input());

for i in range(testCase):
  [x_app,y_app] = [int(n) for n in input().split()]
  print(needScreen(x_app,y_app));
