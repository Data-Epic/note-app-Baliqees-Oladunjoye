import datetime
class Note:
    def __init__(self, content, created_at, note_details):
        """Initialize a note with a content and created_at(The  timestamp when the note was added) """
        self.content = content
        self.created_at = created_at
        self.note_details = note_details
    
    def display(self):
        """display(a method to show note details) """
        return ("self.content","self.created_at")
    
class TextNote(Note):
    def __init__(self, content, created_at, text_based_note):
        Note.__init__(self, content,created_at)
        self.text_based_note = text_based_note

    def display(self):
        '''overrinding the display method in the parent class'''
        print(self.content, self.created_at, self.text_based_note)

class ReminderNote(Note):
    def __init__ (self, content, created_at, reminder_date, reminder_time):
        Note.__init__(self, content, created_at)
        self.reminder_date = reminder_date
        self.reminder_time = reminder_time
    def display(self):
        '''overrinding the display method in the parent class'''
        print(self.reminder_date, self.reminder_time)

    
class NoteManager:
    def __init__(self):
        '''starting with an empty note'''
        self.note = {} #every note will be stored here
        self.note_id_counter = 1 # this will generate a unique id for each note
    def add_note(self, note_type, content, reminder_time=None): 
        '''Adds a new note with a unique id'''
        note_id = self.note_id_counter
        self.note[note_id] = {"type":note_type, "content":content, "reminder_time":reminder_time, 
                              "created_at":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.note_id_counter += 1 #increase the counter for the next note
        print(f'Note {self.note[note_id]} added successfully')
        return self.note[note_id]  # Ensure this line returns the note
    def delete_note(self, note_id):
        '''delete a note by id'''
        if note_id in self.note:
            del self.note[note_id]
            print (f'Note {note_id} deleted successfully')
        else:
            print(f'Note {note_id} not found')

    def show_note(self, note_id):
        """Retrieve a specific note by ID."""
        if note_id in self.note:
            return {note_id: self.note[note_id]}
        else:
            raise KeyError(f"Note ID {note_id} does not exist.")
    

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
    
    def search_note(self, keyword):
        matching_notes = {}
        for note_id, note in self.note.items():
            if keyword.lower() in note["content"].lower():
                matching_notes[note_id] = note

        return matching_notes  # Return the matching notes