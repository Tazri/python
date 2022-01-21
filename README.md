![github](./asset/badge/github.svg) ![python](./asset/badge/python-programming.svg) ![documentation](./asset/badge/python-documentation.svg)

# Python Programming Language

This is simple documentation on python programming language. I create this documentation on my way. I try to understand the python in deep and took down documentation.

## Table of Content

- [Basic](#Basic)
  - [Basic Function](#Basic_Function)
  - [Comment](#Comment)
- [Variable](#Variable)
  - [Casting](#Casting)
  - [Multiple_Assign](#Multiple_Assign)
  - [Global_Variable](#Global_Variable)
- [Datatype](#Datatype)
  - [Number](##Number)
  - [Type](##Type)
  - [Random Number](##Random_Number)
- [String](#String)
  - [String Array](##String_Array)
  - [Loop String](##Loop_String)
  - [String Len](##String_Len)
  - [Check String](##Check_String)
  - [String Method](##String_Method)
  - [String Concatenate](##String_Concatenate)
  - [String Format](##String_format)
  - [Escape_Characters](##Escape_Characters)

# Basic

Let's see the basic python program :

**_Porgram : hello, world!_**

```python
print("Hello, World!");
```

**_Output : hello, world!_**

```
Hello, World!
```

### Basic Function

Let's see some built in python basic function :

| Function | Description      |
| -------- | ---------------- |
| print    | print something  |
| input    | input something  |
| int      | convert integare |
| float    | convert float    |
| str      | convert string   |

Python input everything as string.

```python
print("Something print"); # something print

# something input
# input("Something input");

# print number
print(int("30"));

# print float
print(float("40"));

# print string
print(str(40));
```

**_Output_**

```python
Something print
30
40.0
40
```

## Comment

Comment in python is simple. Just use # symbol before the comment. Then python ignore this code. Multiline comment start with ''' and end with ''' or another way is start with """ and end with """.

**_Program : comment_**

```python
# single line comment.

"""
this is a multiline comments
"""

'''
another multiline comments
'''
```

Python will ignore this code.

# Variable

Variable is something which contain value.Rule to use variable :

**_Program : variable_**

```python
variable = "value";

# number type variable
number = 30;

# float type variable
number_float = 30.23;

# string type variable
string = 'This is string';

print(number);
print(number_float);
print(string);
```

**_Output : variable_**

```
30
30.23
This is string
```

**_Rule to take variable name :_**

1. Variable name can not start with number
1. Can not include speacial symbol ("#@!))
1. Can not use reserve keyword
1. Can not include space

## Casting

In python we can casting variable.

| Casting Keyword | work             |
| --------------- | ---------------- |
| int             | convert integare |
| float           | convert float    |
| str             | convert float    |

**_Program : variable_**

```python
# convert integare
print(int("30"));

# convert float
print(float(30));

# convert string
pritn(str(30302));
```

**_Output : variable_**

```
30
30.0
30302
```

## Multiple Assign

In python we can assign variable mutliple value in one time.

**_Program : multiple assign_**

```python
x,y,z = 32,31,23;
list = ['Apple','Benana','Mango'];
a,b,c = list;

print(">>> x y z <<<");
print("> x : " + str(x));
print("> y : " + str(y));
print("> z : " + str(z));

print("\n>>> a b c <<<");
print("> a : " + a);
print("> b : " + b);
print("> c : " + c);
```

**_Output : multiple assign_**

```
>>> x y z <<<
> x : 32
> y : 31
> z : 23

>>> a b c <<<
> a : Apple
> b : Benana
> c : Mango
```

## Global_Variable

Global vriable is which can declear outside the function. If we can access global variable inside the function with global keyword.

**_Program : global variable_**

```python
# create global variable inside the function
def one():
    global x;
    x = "This is global Variable.";
def two():
    global x;
    x = "This is changing global Variable."

# calling function
one();
print("x : "+x);

# changing global variable by calling function
two();
print("x : "+x);
```

**_Output : global variable_**

```
x : This is global Variable.
x : This is changing global Variable.
```

# Datatype

Python have lot's of datatype.In here list of datatype in python.

| Datatype      | Type                        |
| ------------- | --------------------------- |
| Text Type     | str                         |
| Numeric       | int,float,complex           |
| Sequence      | list,tuple,range            |
| Mapping Type  | dict                        |
| Set Types     | set, frozenset              |
| Boolean Types | bool                        |
| Binary Types  | bytes,bytesarray,memoryview |

Let's see text,numeric, sequence and boolean datatypes :

**_Program : some datatype_**

```python
# numberic type
int_number = 30;
float_number = 32;
complex_number = 321j;

print("int : ",int_number);
print("float : ",float_number);
print("complex_number : ",complex_number);

# text type
string = "Md Tazri";
print("string : ",string);

# Boolean type
boolean = True;
print("Boolean : ",boolean);

# sequence type
list = [32,21,"Tazri"];
tuple = {32,21,21};
range_type = range(5);
print("List : ",list);
print("tupple : ",tuple);
print("range :",range);
```

**_Output : some datatype_**

```
int :  30
float :  32
complex_number :  321j
string :  Md Tazri
Boolean :  True
List :  [32, 21, 'Tazri']
tupple :  {32, 21}
range : <class 'range'>
```

## Number

Python have 3 type of number type variable.

- Integare (int)
- Float (float)
- Complex (complex)

We already see who to use those number. Now we see how to typecasting.

**_Program : number typecasting_**

```python
number_int = int("32");
number_float= float(32);
number_complex = complex(3222342332432435435345324435324523423);

print("number int : ",number_int);
print("number float : ",number_float);
print("number complex : ",number_complex);
```

**_Output : number typecasting_**

```
number int :  32
number float :  32.0
number complex :  (3.222342332432435e+36+0j)
```

## Type

type function to see the type of data. It's show the class name. Let's see example :

**_Program : type_**

```python
number_int = int("32");
number_float= float(32);
number_complex = complex(3222342332432435435345324435324523423);

print(type(number_int),": ",number_int);
print(type(number_float),": ",number_float);
print(type(number_complex),": ",number_complex);
```

**_Output : type_**

```
<class 'int'> :  32
<class 'float'> :  32.0
<class 'complex'> :  (3.222342332432435e+36+0j)
```

## Random_Number

If we create random number in pythen then we first import random library. Which is python builtin library.

**_Syntax :_**

```
import random
random.randrange(start,end)
```

**_Program : random number_**

```python
import random;

# number from 1 to 10
print(random.randrange(1,10));

# number from 5 to 106 int
print(random.randrange(5,106));
```

**_Output : random number_**

```
9
70
```

# String

String is which text is start single or double qoutation and end with it. Even if it call string if nothing is double and single qoutation.

**_Program : simple string_**

```python
double_qoute_string = "This is a string with double qoute";

single_qoute_string = 'This is a string with single qoute';

three_qoute_string = '''
This is a string with single qoute.
'''

three_double_qoute_string = """
This is a string with three double qoute.
"""

print(double_qoute_string);
print(single_qoute_string);
print(three_qoute_string);
print(three_double_qoute_string);
```

**_Output : simple string_**

```
This is a string with double qoute
This is a string with single qoute

This is a string with single qoute.


This is a string with three double qoute.

```

## String_Array

We can access string like array.

**_Syntax access string element_**

```
string = "name"

in here every element index is
n = 0
a = 1
m = 2
3 = 3

access 3nd element like
string[2]

access like
string[index]
```

**_Speacify access string element_**

```
string = "name"
string[index];
string[-2]; mean it count reverse

reverse index
e = -1
m = -2
a = -3
n = -4
```

**_Select Range syntax_**

```
string = "name"
string[start_index : end_index];

by default,
start_index = 0
end_index = -1

string[1:]
output : "ame"
string[1:3]
output : "am"
```

**_Select Reverse syntax_**

```
string = "name"
string[::-1]
it print the string reverse
output : "eman"
```

**_Program : access string array_**

```python
name = "Md Tazri";

print("name : ",name);
print("name[0] : ",name[0]);
print("name[-1] : ",name[-1]);
print("name[2:] : ",name[2:]);
print("name[:3] : ",name[:3]);
print("name[3:-2] :",name[3:-2]);
print("name[::-1] : ",name[::-1]);
```

**_Output : access string array_**

```
name :  Md Tazri
name[0] :  M
name[-1] :  i
name[2:] :   Tazri
name[:3] :  Md
name[3:-2] : Taz
name[::-1] :  irzaT dM
```

**_Important thing about string_**

1. String act like array only access element case.
1. We can not change string element.
1. String is unmutable in python.

## Loop String

We also traverse string with loop.

**_Program : loop string_**

```python
my_name = "Md Tazri";

for l in my_name :
    print("Letter ",l);
```

**_Output : loop string_**

```
my_name = "Md Tazri";

for l in my_name :
    print("Letter ",l);
```

## String_Len

We can see string length by len function.

**_Program : string len_**

```python
name = "Md Tazri";
print("len(name) : ",len(name));
```

**_Output: string len_**

```
len(name) :  8
```

## Check String

'in' and 'not in' character to check substring exist in another string.

**_Syntax :_**

```
string = 'something write';
sub_string = 'sub';

# checking
sub_string in string;
## if sub_string exist in string it must be return true other way it return false.

sub_string not in string;
## if sub_string can not exist in string it must be return true other wish it return false.
```

**_Program : check string_**

```python
sentence = "My name is tazri and i live in comilla.";

print("sentence : ");
print(sentence);
print("'tazri' in sentence : ");
print('tazri' in sentence);
print("'focus' in sentence : ");
print('focus' in sentence);
print("'focus' not in sentence : ");
print('focus' not in sentence);
print("'tazri' not in sentence : ");
print('tazri' not in sentence);
```

**_Output : check string_**

```
My name is tazri and i live in comilla.
'tazri' in sentence :
True
'focus' in sentence :
False
'focus' not in sentence :
True
'tazri' not in sentence :
False
```

## String_Method

Here some string method :
| Method | work |
|--------------|-----------------------------------|
| capitalize | convert first letter uppercase |
| lower | convert string lower case |
| upper | convert string upper case |
| title | convert string like header |
| casefold | convert string lower case |
| count | search subtring how many time |
| find | return start position of sub str |
| replace | it replace old sub string by new sub string |
| strip | remove white space from start to end |

**_Program : string methods 1_**

```python
sentence = "my name is Md Tazri and I am Student.Do you know me ? i want to be a programmer.";

print("sentence : ");
print(sentence);

# make capital first letter
print("\n\nsentence.capitalize()");
print(sentence.capitalize());

# make string upper
print("\n\nsentence.upper()");
print(sentence.upper());

# make string lower case
print("\n\nsentence.lower()");
print(sentence.lower());

# make string title
print("\n\nsentence.title() : ");
print(sentence.title());

# make string lowercase by casefold
print("\n\nsentence.casefold() : ");
print(sentence.casefold());

# count i how many time
print("\n\nsentence.count('i') : ");
print(sentence.count('i'));

# count 'name' string position 0 to 8
print("\n\nsentence.count('name',0,8)");
print(sentence.count('name',0,8)); ## by default start is 0 and end is -1

# find 'tazri' in string
print("\n\nsentence.find('tazri') : ");
print(sentence.find('tazri'));

# find 'Tazri' in string
print("\n\nsentence.find('Tazri') : ");
print(sentence.find('Tazri'));

# saytax of find is :
# find(value,start_index,end_index);
# by default start = 0 and end is -1
# it return start position of sub_string in string
# if return -1 if sub_string not exist in string
```

**_Output : string method 1_**

```
sentence :
my name is Md Tazri and I am Student.Do you know me ? i want to be a programmer.


sentence.capitalize()
My name is md tazri and i am student.do you know me ? i want to be a programmer.


sentence.upper()
MY NAME IS MD TAZRI AND I AM STUDENT.DO YOU KNOW ME ? I WANT TO BE A PROGRAMMER.


sentence.lower()
my name is md tazri and i am student.do you know me ? i want to be a programmer.


sentence.title() :
My Name Is Md Tazri And I Am Student.Do You Know Me ? I Want To Be A Programmer.


sentence.casefold() :
my name is md tazri and i am student.do you know me ? i want to be a programmer.


sentence.count('i') :
3


sentence.count('name',0,8)
1


sentence.find('tazri') :
-1


sentence.find('Tazri') :
14
```

**_Program : String Methods 2_**

```python
sentence = "My name is md Tazri and I am a simple students nothing else.";
tuple = ('black','yellow','red','dry');


print("sentence : ");
print(sentence);

# replase
'''
replace sayntax
string.replace(value,new_value,count)

by default it replace all old value by new value other wish it replace count time.
'''

print("\n\nsentence.replace('s','t') : ");
print(sentence.replace('s','t'));

print("\n\nsentence.replace('m','l',2) : ");
print(sentence.replace('m','l',2));

# swapcase()
# swapcase return the string where all letter swap from upper to lower and lower to upper.

print("\n\nsentence.swapcase() : ");
print(sentence.swapcase());

# join()
# take iterable object and it join them as string by some thing
# syntax
# value.join(tuple)
# it joint by value every element of iterable object

print("\n\ntuple : ");
print(tuple);
print("\n\n''.join(tuple) : ");
print(''.join(tuple));

print("\n\n'--> '.join(tuple) :");
print('--> '.join(tuple));
```

**_Output : string methods 2_**

```
sentence :
My name is md Tazri and I am a simple students nothing else.


sentence.replace('s','t') :
My name it md Tazri and I am a timple ttudentt nothing elte.


sentence.replace('m','l',2) :
My nale is ld Tazri and I am a simple students nothing else.


sentence.swapcase() :
mY NAME IS MD tAZRI AND i AM A SIMPLE STUDENTS NOTHING ELSE.


tuple :
('black', 'yellow', 'red', 'dry')


''.join(tuple) :
blackyellowreddry


'--> '.join(tuple) :
black--> yellow--> red--> dry
```

**_Program : string methods 3_**

```python
sentence = "      this is string ";

# strip
# remove white spacess from start and end.
print("sentence : ");
print(sentence);

print("\n\nsentence.strip() : ");
print(sentence.strip());
```

**_Output : string methods 3_**

```
sentence :
      this is string


sentence.strip() :
this is string
```

## String_Canecatenate

We can use + operator to canecatenate more than one string. Let's

**_Program : string canecatenate_**

```python
string_one = "Md";
space = " " ;
string_two = "Tazri";

print(string_one+space+string_two);
```

**_Output : string canecatenate_**

```
Md Tazri
```

## String_Format

format is builtin string function which can use for formating string in my own way.

**_Program : string format_**

```python
sentence = "Hey, I {} {} and I am {} year old's.";
sentence_two = "Hey, I am {2} {1} and I am {0} year old's.";
first_name = "Md";
last_name = "Tazri";
age = 17;

print("sentence : ");
print(sentence);

print("\n\nsentence.format(first_name,last_name,age) : ");
print(sentence.format(first_name,last_name,age));

print("\n\nsentence_two : ");
print(sentence_two);

print("\n\nsentence_two.format(age,last_name,first_name) : ");
print(sentence_two.format(age,last_name,first_name));
```

**_Output : string format_**

```
sentence :
Hey, I {} {} and I am {} year old's.


sentence.format(first_name,last_name,age) :
Hey, I Md Tazri and I am 17 year old's.


sentence_two :
Hey, I am {2} {1} and I am {0} year old's.


sentence_two.format(age,last_name,first_name) :
Hey, I am Md Tazri and I am 17 year old's.
```

## Escape_Characters

Here list of escape character in python :

| Character | Description           |
| --------- | --------------------- |
| \'        | print single quote    |
| \"        | print double quote    |
| \\        | print backslash       |
| \n        | print new line        |
| \t        | print tab             |
| \b        | print backspace       |
| \1oo      | for octal value       |
| \xhh      | for hexadecimal value |

**_Program : escape character_**

```python
print("single quote here \'. new line \n double quote here \"")
print("backslash \\");
print("tab \tspace");
print("back \bspace (\\b)");
print("otacl code \133\134");
print("hexa code \x32 \x25");
```

**_Output : escape character_**

```
single quote here '. new line
 double quote here "
backslash \
tab 	space
backspace (\b)
otacl code [\
hexa code 2 %
```

## Arithmetic_Operator

We can use arithmetic operator python as well but in here we can extra two arithmetic operator.

**_Arithmetic Operator:_**
| Operator | Work |
| -------- | -------------------------- |
| + | Addition |
| - | Subtraction |
| / | Division |
| \* | Multiplication |
| % | Remainder(Modulos) |
| // | (new) Floor Division |
| \*\* | Exponentiation |
