from pyscript import document

# This function runs when the button is clicked
def validate_account(event):

    # Get the value entered in the username input field
    UsernameInput = document.getElementById("username").value

    # Get the value entered in the password input field
    PasswordInput = document.getElementById("password").value

    # Get the result <div> where messages will be displayed
    SignUpResult = document.getElementById("result")

    # Create an empty list to store error messages
    ErrorMessages = []


    # -------------------------
    # USERNAME VALIDATION
    # -------------------------

    # Check if username length is less than 7 characters
    if len(UsernameInput) < 7:

        # Calculate how many characters are needed
        Username_remaining = 7 - len(UsernameInput)

        # Add message to the list
        ErrorMessages.append(f"Username needs {Username_remaining} more character(s).")


    # -------------------------
    # PASSWORD LENGTH CHECK
    # -------------------------

    # Check if password length is less than 10 characters
    if len(PasswordInput) < 10:

        # Calculate how many characters are needed
        Password_remaining = 10 - len(PasswordInput)

        # Add message to the list
        ErrorMessages.append(f"Password needs {Password_remaining} more character(s).")


    # -------------------------
    # PASSWORD LETTER CHECK
    # -------------------------

    # Count how many letters are inside the password
    # char.isalpha() returns True if the character is a letter
    # char is short for character
    Password_letter_count = sum(1 for char in PasswordInput if char.isalpha())

    # If there are no letters
    if Password_letter_count < 1:
        ErrorMessages.append("Password needs at least 1 letter.")


    # -------------------------
    # PASSWORD NUMBER CHECK
    # -------------------------

    # Count how many digits are inside the password
    # char.isdigit() returns True if the character is a number
    Password_number_count = sum(1 for char in PasswordInput if char.isdigit())

    # If there are no numbers
    if Password_number_count < 1:
        ErrorMessages.append("Password needs at least 1 number.")


    # -------------------------
    # FINAL RESULT DISPLAY
    # -------------------------

    # If there are any messages in the list,
    # it means some requirements are not satisfied
    if ErrorMessages:

        # Apply Bootstrap styling for error (red text)
        SignUpResult.className = "mt-3 text-danger fw-bold"

        # Join all error messages into one string with line breaks
        SignUpResult.innerHTML = "<br>".join(ErrorMessages)

    else:
        # If no errors, it means all conditions are satisfied

        # Apply success styling (green text)
        SignUpResult.className = "mt-3 text-success fw-bold"

        # Display success message

        SignUpResult.innerHTML = "Account successfully created!"
