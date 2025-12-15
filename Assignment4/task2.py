'''Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''


text = input("Enter text to write to the file : ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written in output.txt .\n")

append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.\n")

print("Final content of the output.txt :")
with open("output.txt", "r") as file:
    print(file.read())
