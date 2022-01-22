fruits = ['apple','orange','mango','benana'];
basket = [];

'''
user list comprenhension syntax
[item for item in list];
return a array
'''

print("fruits : ");
print(fruits);
print("basket : ");
print(basket);
basket = [item for item in fruits];
print("basket after comprehension : ");
print(basket);

'''
we can set here condition as well :
[item for item in list if condition == true]
'''
print("we can apply on range, here : ");
print([n for n in range(10) if not(n & 1)]);

'''
we can apply any operation first like :
[item_with_operation for item in list if condition];
'''
print([fruit.upper() for fruit in fruits if fruit != 'benana']);
