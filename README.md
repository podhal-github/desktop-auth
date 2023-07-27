# desktop-auth

The Python Login and Registration GUI is a desktop application that provides a graphical user interface (GUI) for users to log in or register for an account. The application uses the tkinter library for the GUI, PIL (Pillow) for image handling, and interacts with a MySQL database to store user account information. Users can log in with existing accounts or create new accounts with a login and password. 

# Usage:

1. Make sure you have Python installed on your computer.

2. Install the required libraries by running the following command in the terminal or command prompt:
```pip install tkinter mysql-connector-python pillow```

3. Place the Python script and the image files (background.png, editbox.png, and button.png) in the same directory.

4. Run the Python script using the command: ```python main.py```

5. The GUI window will open, displaying a background image, login and password input fields, and "Login" and "Register" buttons.

# Functionality:

Log In: Enter your existing login and password in the input fields and click the "Login" button to log in.

Register: If you don't have an account, enter your desired login and password in the input fields and click the "Register" button to create a new account.

# Database Structure:

The provided SQL dump includes a single table named accounts. The table has the following columns:

1. id (INT): Auto-incrementing primary key to uniquely identify each account.
2. nickname (TEXT): The nickname of the user (currently not used in the script).
3. login (TEXT): The login (username) of the user.
4. password (TEXT): The password of the user (currently stored in plain text, not recommended for production use).
5. money (INT): An integer field to store the user's money balance.

# Additional Notes:
1. The provided SQL dump includes a single test account with the login "Test" and password "12345". You can modify this data or add more accounts as needed.
2. The script uses tkinter to create a basic GUI, but you can enhance the design and layout as per your preferences.
