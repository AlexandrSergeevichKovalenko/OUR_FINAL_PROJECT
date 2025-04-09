from collections import UserDict
class Note:
    def __init__(self, title, note = None):
        self.title = title
        self.tags = set()
        self.note = note

    def add_note(self, note):
        self.note = note

    def add_tags(self, tags):
        self.tags.update(tags)

    def __str__(self):
        if self.tags:
            tags = sorted(list(self.tags))
            return (f"""{"✨"} Title: {self.title}
{"📜"} Note: {self.note}
{"🏷️"} Tage: {" ".join(tag+"," for tag in tags)}""")
        else:
            return (f"""{"✨"}Title: {self.title}
{"📜"}Note: {self.note}""")

class NoteBook(UserDict):
    def add_record(self, note: Note):
        """Add a Note instance to the notebook."""
        self.data[note.title] = note

    def find(self, title: str) -> Note:
        """Find a note by title. Returns the Note or None."""
        if title in self.data:
            return self.data[title]
        return None

    def delete(self, title:str) -> None:
        """Delete a note by title, if it exists."""
        if title in self.data:
            del self.data[title]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())