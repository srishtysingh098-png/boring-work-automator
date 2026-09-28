from file_organizer import organize_files
from bulk_renamer import rename_files
from report_generator import generate_report


def main():
    while True:
        print("\n===== BORING WORK AUTOMATOR =====")
        print("1. Organize files")
        print("2. Rename files")
        print("3. Generate file report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            organize_files()
        elif choice == "2":
            rename_files()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
