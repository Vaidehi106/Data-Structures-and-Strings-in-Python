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
