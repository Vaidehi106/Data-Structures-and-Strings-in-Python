# Task 1: Create a Dictionary of Student Marks

1.  **Student Marks Dictionary:**
    * The script initializes a dictionary named `dict`.
    * This dictionary stores student names as keys (e.g., 'vedu', 'vanshu') and their respective marks as integer values (e.g., 97, 93).

2.  **User Input:**
    * The script prompts the user to "enter your name:".
    * The user's input (the student's name) is read from the console and stored in the variable `user`.

3.  **Marks Retrieval and Display:**
    * The script checks if the entered `user` name exists as a key within the `dict` dictionary using the `in` operator.
    * **If the student's name is found:**
        * The script uses the `dict.get(user)` method to retrieve the marks associated with the entered name.
        * The retrieved marks are then printed to the console.
    * **If the student's name is not found:**
        * The script executes the `else` block.
        * A message "Student not found" is printed to the console, indicating that the entered name is not present in the student marks dictionary.

# Task 2: Demonstrate List Slicing 

1.  **Creates a List of Numbers:**
    * The script initializes a list named `list` containing the integers from 1 to 10 in ascending order: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

2.  **Extracts the First Five Elements:**
    * Using list slicing (`list[0:5:1]`), the script extracts the first five elements from the `list`.
    * The slice starts at index 0 (inclusive) and goes up to index 5 (exclusive), with a step of 1.
    * The extracted elements `[1, 2, 3, 4, 5]` are stored in a new list named `slicing`.

3.  **Reverses the Extracted Elements:**
    * Using list slicing with a step of `-1` (`slicing[::-1]`), the script creates a reversed copy of the `slicing` list.
    * The reversed elements `[5, 4, 3, 2, 1]` are stored in a new list named `reversing`.

4.  **Prints the Results:**
    * The script prints the original `list` (after converting it to a string).
    * It then prints the `slicing` list (the first five elements, also converted to a string).
    * Finally, it prints the `reversing` list (the reversed first five elements, converted to a string).
