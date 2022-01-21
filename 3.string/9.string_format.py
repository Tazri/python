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