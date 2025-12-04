#Let's Practice Sets In Python

class_set = {"Maths", "Science", "English", "History"}
print(class_set);

#Duplicates are not allowed in sets

#Adding New Element
class_set.add("Geography");

#Empty Set
empty_set = set()
print(empty_set);

#Set Methods
class_set.add("Kunafa");


#Union And Intersection
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b));
print(set_a.intersection(set_b));

#Practice Questions
programming_lists= ["Python", "Java", "C++", "Python", "JavaScript", "C++", "Java"]
unique_programming_languages = set(programming_lists)
print(unique_programming_languages);
print(type(unique_programming_languages));