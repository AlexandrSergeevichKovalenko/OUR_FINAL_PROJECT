from functions_block import load_data, save_data, FILENAME, NOTEFILENAME
from interactive_menu import InteractiveMenu


if __name__ == '__main__':
    book = load_data(FILENAME)
    notebook = load_data(NOTEFILENAME)
    menu = InteractiveMenu()

    try:
        menu.run(book, notebook)
    finally:
        save_data(book, FILENAME)
        save_data(notebook, NOTEFILENAME)
