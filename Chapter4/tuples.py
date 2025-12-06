#Tuples
tuple1 = ("Apple", "Banana", "Cherry");
print(tuple1);
print(tuple1[0]);  # Accessing first element
print(tuple1[2]);  # Accessing third element
print(tuple1[-1]); # Accessing last element
#Tuple Slicing
print(tuple1[0:2]);  # From index 0 to 1
print(tuple1[:2]);   # From start to index 1
print(tuple1[1:]);   # From index 1 to end
print(len(tuple1));  # Length of the tuple

#Indexing
print(tuple1[1]);  # Banana


#Tuples Are Immutable
# tuple1[0] = "Grapes";  # This will raise an error

#Take 3 Cities From User And Store In Tuple
city1 = input("Enter First City: ");
city2 = input("Enter Second City: ");
city3 = input("Enter Third City: ");
city_tuple = (city1, city2, city3);
print("Your City Tuple Is: ", city_tuple);
print("Length Of Your City Tuple Is: ", len(city_tuple));

#Practice Question

Fruits = ("Apple", "Banana", "Mango", "Orange", "Pineapple");
print("Fruits Tuple: ", Fruits);
print(len(Fruits));
print(Fruits[1]);  # Accessing second fruit
print(Fruits[2:4]);  # Slicing from index 2 to 3


#Practice Assignments

Movie1 = input("Enter First Movie Name: ");
Movie2 = input("Enter Second Movie Name: ");
Movie3 = input("Enter Third Movie Name: ");
movies_list = [Movie1, Movie2, Movie3];
movies_tuple = (Movie1, Movie2, Movie3);
print("Your Movies List Is: ", movies_list);
print("Your Movies Tuple Is: ", movies_tuple);

# 2nd Assignment
marks = (85, 90, 78, 92, 88);
print("Marks Tuple: ", marks);
print(max(marks));  # Highest Marks
print(min(marks));  # Lowest Marks
print(sum(marks));  # Total Marks
print(len(marks));  # Number of Subjects


#3rd Assignment
#Write A Program To Check Grade Based On Marks Stored In Tuple
student_marks = (95, 67, 82, 74, 59);
for i, mark in enumerate(student_marks):
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Student {i+1} Marks: {mark}, Grade: {grade}");