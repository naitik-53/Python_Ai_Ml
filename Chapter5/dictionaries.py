#Dictionary is a built in datatype in python used to store data in key-value pairs.

student1 = {
    "name": "John",
    "age": 20,
    "courses" : ["Maths", "Science"]
}

print(student1);

#Indexing Does Not Work In Dictionaries
#print(student1[0]) # This will raise an error
#this means they are unordered

print(student1["name"]);
print(student1["age"]);


#Adding New Key-Value Pair
student1["Class"] = "12th Grade"
print(student1);

#Modifying Existing Key-Value Pair
student1["age"] = 17
print(student1);

#Dictionary Methods
print(student1.keys());
print(student1.values());
print(student1.items());

student1["age"] = 18
print(student1.get("age")); #Using get method to access value

#Practice Questions

marks = {
    "Maths": 95,
    "Science": 90,
    "English": 85
}
print(marks);

marks["History"] = 88
marks["Civics"] = 98
print(marks);

marks.pop("English");
print(marks);


