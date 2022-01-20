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

#Basic
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

#Datatype
