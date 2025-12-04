#Lists In Python

fruits = ["Apple", "Banana", "Mango", "Orange"];
print(fruits);
print(fruits[0]);  # Accessing first element
print(fruits[2]);  # Accessing third element    
print(fruits[-1]); # Accessing last element

#Modifying List Elements
fruits[1] = "Grapes";
print(fruits);

#List Slicing
print(fruits[1:3]);  # From index 1 to 2
print(fruits[:2]);   # From start to index 1
print(fruits[2:]);   # From index 2 to end

print(len(fruits));  # Length of the list

fruits.append("Pineapple");  # Adding an element at the end
print(fruits);
fruits.remove("Mango");      # Removing an element
print(fruits);
fruits.pop();                # Removing the last element
print(fruits);
fruits.insert(1, "Strawberry");  # Inserting at index 1
print(fruits);
fruits.sort();              # Sorting the list
print(fruits);

#Take 3 Food From User And Store In List 

food1 = input("Enter First Food Item: ");
food2 = input("Enter Second Food Item: ");
food3 = input("Enter Third Food Item: ");
food_list = [food1, food2, food3];
print("Your Food List Is: ", food_list);
print("Length Of Your Food List Is: ", len(food_list));