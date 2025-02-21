import datetime
class Note:
    def __init__(self, content, created_at):
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
    def delete_note(self, note_id):
        '''delete a note by id'''
        if note_id in self.note:
            del self.note[note_id]
            print (f'Note {note_id} deleted successfully')
        else:
            print(f'Note {note_id} not found')
    
    def show_note(self):
        """Displays all notes"""
        if self.note:
            print("\n📜 All Notes:")
            for note_id, note in self.note.items():
                print(f'ID: {note_id}, Type: {note["type"]}, Content: {note["content"]}, Created: {note["created_at"]}')
        else:
            print("\n📭 No notes available!\n")


    def search_note(self, keyword):
        """Finds notes that contain a specific keyword in their content."""
        found_notes = [note for note_id, note in self.note.items() if keyword.lower() 
                       in note["content"].lower()]
        if found_notes:
            print(f'Notes containing "{keyword}":')
            for note in found_notes:
                print(f"- {note['type']}: {note['content']}")
        else:
            print(f'No notes found with keyword "{keyword}".')

