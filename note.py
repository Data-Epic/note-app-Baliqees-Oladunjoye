class Note:
    def __init__(self, content, created_at, note_details):
        """Initialize a note with a content, create_at(The  timestamp when the note was added) 
        and note_details (A display() method to show note details)"""
        self.content = content
        self.created_at = created_at
        self.note_details = note_details
    
