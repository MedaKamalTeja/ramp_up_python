import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z.]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def write_emails_to_file(email_list):
    with open('email_list.txt', 'w') as file:
        for email in email_list:
            file.write(email + '\n')
    print("Emails written to the file.")

def main():
    email_list = []

    while True:
        user_input = input("New email? (Yes/No):").strip().lower()

        if user_input == 'no':
            if email_list:
                write_emails_to_file(email_list)
            else:
                print("No valid emails to write.")
            break
        elif user_input == 'yes':
            user_email = input("Enter an email address: ").strip()
            if validate_email(user_email):
                email_list.append(user_email)
                print("Email is valid. Added to the list.")
            else:
                print("Invalid email address. Please enter a valid email.")
        else:
            print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    main()
