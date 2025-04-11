from functions_block import load_data
from interactive_menu import InteractiveMenu
from note_functions import load_notes, save_notes

if __name__ == '__main__':
    book = load_data()
    notebook = load_notes()
    menu = InteractiveMenu()
    try:
        menu.run(book, notebook)
    finally:
        save_notes(notebook)
