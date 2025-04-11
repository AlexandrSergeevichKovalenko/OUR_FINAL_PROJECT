from functions_block import load_data, save_data
from interactive_menu import InteractiveMenu
from classes_for_program import *

if __name__ == '__main__':
    book = load_data(FILENAME)
    notebook = load_data(NOTEFILENAME)
    menu = InteractiveMenu()

    try:
        menu.run(book, notebook)
    finally:
        save_data(notebook, NOTEFILENAME)
        save_data(book, FILENAME)
