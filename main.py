import menu

def main():
    while True:
        print("\n***** Welcome to Clinic Management System *****)")
        print("1. Receptionist")
        print("2. Doctor")
        print("3. Exit")
        user_type = input("Select user type: ")

        if user_type == "1":
            if menu.receptionist_login():
                menu.reception_menu()
        elif user_type == "2":
            if menu.doctor_login():
                menu.doctor_menu()
        elif user_type == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
