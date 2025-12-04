#This Is My First Python Project
#Student Report Card System

#Taking Student Name And Marks As Input
student_name = input("Enter Student Name : ");
roll_number = int(input("Enter Your Roll Number : "));
maths_marks = int(input("Enter Marks Obtained In Maths : "));
science_marks = int(input("Enter Marks Obtained In Science : "));
english_marks = int(input("Enter Marks Obtained In English : "));
hindi_marks = int(input("Enter Marks Obtained In Hindi : "));
social_studies_marks = int(input("Enter Marks Obtained In Social Studies : "));

#Calculating Total Marks And Percentage
total_marks = maths_marks + science_marks + english_marks + hindi_marks + social_studies_marks;
percentage = (total_marks / 500) * 100;

#Determining Grade Based On Percentage
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
else:
    grade = 'F'

#Printing The Report Card
print("\n----- Student Report Card -----");
print("Name          : ", student_name);
print("Roll Number   : ", roll_number);
print("Maths         : ", maths_marks);
print("Science       : ", science_marks);
print("English       : ", english_marks);
print("Hindi         : ", hindi_marks);
print("Social Studies: ", social_studies_marks);
print("Total Marks   : ", total_marks);
print("Percentage    : ", percentage);
print("Grade         : ", grade);

print("-------------------------------\n");

#Let's Store The Data In A Tuple
student_report = (student_name, roll_number, maths_marks, science_marks, english_marks, hindi_marks, social_studies_marks, total_marks, percentage, grade);

#I will not print the tuple here to avoid redundancy



#------End Of The Program--------


