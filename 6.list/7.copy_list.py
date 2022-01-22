# we can not copy list by list_one = list_two
# Example : 
name_list = ['Tazri','Focasa','Troy','Farha','Solus','Xenon'];
name_list_two = name_list;

print('name_list : ',name_list);
print('name_list_two : ',name_list_two);

# changing name_list_two and see what heppen inside the name_list 
name_list_two[0] = 'Anonymous';
print('name_list : ',name_list);