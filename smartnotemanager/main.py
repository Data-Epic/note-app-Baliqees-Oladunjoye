from smartnotemanager.note import Note #import the Note class
from smartnotemanager.note import NoteManager #import NoteManager
import datetime


def main():
    manager = NoteManager()
    
    while True:
        print("\n=== Welcome to Smart Notes Manager ===")
        print(" 1 Add a Note")
        print(" 2 Delete a Note")
        print(" 3 Search Notes")
        print(" 4 View All Notes")
        print(" 5  Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            note_type = input("Enter note type (e.g., Work, Personal): ")
            content = input("Enter note content: ")
            manager.add_note(note_type, content)

        elif choice == "2":
            note_id = int(input("Enter note ID to delete: "))
            manager.delete_note(note_id)

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            manager.search_note(keyword)

        elif choice == "4":
            manager.show_note()

        elif choice == "5":
            print("\n Goodbye! Exiting the Notes Manager.")
            break

        else:
            print("\n  Invalid choice! Please select a valid option.\n")

# Ensure the script runs when executed
if __name__ == "__main__":
    main()

