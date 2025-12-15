''' Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

original_list = list(range(1,11))
extracted_list = original_list[:5]
reversed_list = extracted_list[::-1]
print(f"Original list: {original_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")