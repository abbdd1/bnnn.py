'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import time

def send_message(sender, receiver, message):
    try:
        # Code to send the message
        print(f"Message sent from {sender} to {receiver}: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

def receive_message(receiver):
    try:
        # Code to receive the message
        print(f"Message received by {receiver}")
    except Exception as e:
        print(f"Error receiving message: {e}")

def create_group(group_name, members):
    try:
        # Code to create a group
        print(f"Group {group_name} created with members: {members}")
    except Exception as e:
        print(f"Error creating group: {e}")

def add_contact(name, number):
    try:
        # Code to add a contact
        print(f"Contact {name} added with number: {number}")
    except Exception as e:
        print(f"Error adding contact: {e}")

def main():
    # Code to run the application
    pass

if __name__ == "__main__":
    main()