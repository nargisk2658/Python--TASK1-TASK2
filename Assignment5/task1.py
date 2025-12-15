''' Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.


Expected Output:
  Enter the student's name: Alice 
 Alice's marks: 85
If the student does not exist in the dictionary:
 Enter the student's name: John
Student not found.
'''

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88
    }
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
