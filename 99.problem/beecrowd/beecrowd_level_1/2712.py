def get_day(key):
    if key in "12" :
        return "Monday";
    elif key in "34":
        return "Tuesday";
    elif key in "56":
        return "Wednesday";
    elif key in "78":
        return "Thursday"
    elif key in "90":
        return "Friday";
    else:
        return False;


# function to check is valid number plate
def is_valid(plate):
    digits = "0123456789";
    words = plate.split("-");

    if(len(words) != 2):
        return False;

    capital_words = words[0];
    numbers = words[1];

    if len(capital_words) != 3 :
        return False;

    if len(numbers) != 4 :
        return False;

    for char in capital_words:
        if not char.isupper():
            return False;
    
    for digit in numbers:
        if digit not in digits:
            return False;

    return True;

for i in range(int(input())):
    number_plate = input();

    # check is valid number_plate
    if not is_valid(number_plate):
        print("FAILURE");
        continue

    key = number_plate[-1];

    day = get_day(key);

    if day:
        print(day.upper());
    else:
        print("FAILURE");