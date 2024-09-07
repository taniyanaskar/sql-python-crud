from crud_operations import insert_user, fetch_users, update_user, delete_user
from database.py import create_table

# Call this function to set up the database when running the main script
create_table()

def menu():
    while True:
        print("\n1. Insert User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            insert_user(name, email, age)
        elif choice == '2':
            users = fetch_users()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            update_user(user_id, name if name else None, email if email else None, int(age) if age else None)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
if __name__ == "__main__":
    menu()
