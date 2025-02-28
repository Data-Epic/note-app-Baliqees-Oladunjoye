#importing the module
import pytest
import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the NoteManager class
from smartnotemanager.note import NoteManager #importing the class to be tested

@pytest.fixture
def note_manager():
    '''Fixture to create a new NoteManager instance for testing'''
    return NoteManager()

def test_add_note(note_manager):
    '''Test if a note is added correctly'''
    note = note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")

    # Debugging: Print the note to verify its contents
    print(note)

    # Assertions
    assert len(note_manager.note) == 1
    assert note["type"] == "work"
    assert note["content"] == "Prepare slides"
    assert note["reminder_time"] == "2025-02-10 02:00:00"

def test_add_note_without_reminder(note_manager):
    '''Test adding a note without a reminder time'''
    note  = note_manager.add_note('personal', 'prepare food')

    # Debugging: Print the note to verify its contents
    print(note)

    #Assertions
    assert len(note_manager.note) == 1
    assert note['type'] == 'personal'
    assert note['content'] == 'prepare food'
    assert note['reminder_time'] is None 

def test_add_multiple_notes(note_manager):
    '''Test adding multiple notes'''
    note1 = note_manager.add_note('work', 'attend meetings', '2025-03-15 10:00:00')
    note2 = note_manager.add_note('personal', 'attend party')

    print(note1)
    print(note2)

    #Assertions    
    assert len(note_manager.note) == 2
    assert note1['type'] == 'work'
    assert note2['type'] == 'personal'
    assert note1['content'] == 'attend meetings'
    assert note2['content'] == 'attend party'
    assert note1['reminder_time'] == '2025-03-15 10:00:00'
    assert note2['reminder_time'] is None
    assert note_manager.note_id_counter == 3

def test_add_note_with_empty_content(note_manager):
    '''Test adding a note with empty content'''
    note = note_manager.add_note("work", "", "2025-04-10 04:00:00")

    assert len(note_manager.note) == 1
    assert note["type"] == "work"
    assert note["content"] == ""
    assert note["reminder_time"] == "2025-04-10 04:00:00"

def test_add_note_with_duplicate_content(note_manager):
    '''Test adding a note duplicate content'''
    note1 = note_manager.add_note('work', 'attend training', '2025-03-15 10:00:00')
    note2 = note_manager.add_note('work', 'attend training', '2025-03-15 10:00:00')

    assert len(note_manager.note) == 2
    assert note1["content"] == note2["content"]


#Show note testing
def test_show_note(note_manager):
    '''Test showing an existing note'''
    #Add first note
    added_note = note_manager.add_note('work', 'attend training', '2025-03-15 10:00:00')
    note_id = 1  # Assuming the first note has an ID of 1


   # Show all notes
    all_notes = note_manager.show_note(note_id)

    # Verify the note exists in the returned notes
    assert note_id in all_notes
    assert all_notes[note_id] == added_note

def test_show_nonexistent_note(note_manager):
    '''Test showing a note that does not exist'''
    invalid_note_id = 999  # Assuming this ID does not exist

    # Verify that the method raises an exception
    with pytest.raises(KeyError):  # Or ValueError
        note_manager.show_note(invalid_note_id)

def test_show_note_with_reminder(note_manager):
    '''Test showing a note with a reminder i.e, showing note with
    a particular property'''
    # Add a note with a reminder
    note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")
    note_id = 1  # Assuming the first note has ID 1

    # Show the note
    shown_note = note_manager.show_note(note_id)
    print("Returned from show_note:", shown_note)

    # Verify the note has the correct reminder
    assert shown_note.get(note_id, {}).get("reminder_time") == "2025-02-10 02:00:00"


#Delete note testing    
def test_delete_existing_note(note_manager):
        '''Test deleting an existing note'''
        # Add a note first
        note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")
        note_id = 1  # Assuming the first note has ID 1

        # Delete the note
        note_manager.delete_note(note_id)

        # Verify the note is deleted
        with pytest.raises(KeyError):  # Or ValueError, depending on your implementation
            note_manager.show_note(note_id)

def delete_note(self, note_id):
    '''Delete a note by its ID'''
    if note_id not in self.notes:
        raise KeyError(f"Note {note_id} not found")  # Raise KeyError if the note ID does not exist

    # Delete the note
    del self.notes[note_id]
    print(f"Note {note_id} deleted successfully")

def test_delete_only_note(note_manager):
    '''Test deleting the only note'''
    # Add a single note
    note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")
    note_id = 1  # Assuming the first note has ID 1

    # Delete the note
    note_manager.delete_note(note_id)

    # Verify the note is deleted
    assert len(note_manager.note) == 0


#Search note testing
def test_search_note_case_insensitive(note_manager):
    '''Test searching for notes with case-insensitive keywords'''
    # Add a note
    note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")

    # Search for notes using a keyword with different cases
    results = note_manager.search_note(keyword="Slides")

    # Verify the results
    assert len(results) == 1

    # Get the first note from the dictionary
    first_note_id = next(iter(results))  # Get the first key (note ID)
    assert results[first_note_id]["content"] == "Prepare slides"  # Access using the key
    

def test_search_note_with_empty_query(note_manager):
    '''Test searching for notes with an empty query'''
    # Add some notes
    note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")
    note_manager.add_note("personal", "Buy groceries", "2025-02-11 10:00:00")

    # Search with an empty keyword
    results = note_manager.search_note(keyword="")

    # Verify the results (e.g., return all notes or raise an error)
    assert len(results) == 2  # Assuming it returns all notes for an empty query


def test_search_note_with_no_matches(note_manager):
    '''Test searching for notes with no matches'''
    # Add some notes
    note_manager.add_note("work", "Prepare slides", "2025-02-10 02:00:00")
    note_manager.add_note("personal", "Buy groceries", "2025-02-11 10:00:00")

    # Search for notes containing the keyword "nonexistent"
    results = note_manager.search_note(keyword="nonexistent")

    # Verify the results
    assert len(results) == 0
