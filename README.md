# Personal Assistant Console Bot

![Team logo](https://raw.githubusercontent.com/AlexandrSergeevichKovalenko/OUR_FINAL_PROJECT/main/imgs/team_logo.png)

The **Personal Assistant** is a console-based application designed to manage an address book and notes efficiently. The goal is to help users store, search, edit, and manage contacts and notes directly from the terminal. The assistant also includes intelligent features like input validation and natural text interpretation for command suggestions.

---

## 👥 Team

We are a group of students-developers working collaboratively to create a helpful assistant for everyday tasks.

| Name                  | Role                             | GitHub Profile |
|-----------------------|----------------------------------|----------------|
| Kovalenko Oleksandr   | Team Lead / Presenter            | [AlexandrSergeevichKovalenko](https://github.com/AlexandrSergeevichKovalenko) |
| Shadrunov Oleg        | Scrum Master                     | [Oleg-DA7](https://github.com/Oleg-DA7/goit-pycore-hw-08) |
| Shcherbak Oleksii     | Developer 💻 (One of the best)    | [oleksii-shcherbak](https://github.com/oleksii-shcherbak/GoIt/tree/main/homework/goit-pycore-hw-08) |
| Holenok Oleksandr     | Developer 💻 (The other best one) | [4attye](https://github.com/4attye) |

---

## 🎯 Project Goal

To build a system that:
- Stores contact information (names, addresses, phone numbers, emails, birthdays)
- Manages and organizes textual notes with tagging support
- Allows quick search and data retrieval
- Provides smart command suggestions based on user input

---

## ✅ Key Features

### 📇 Contacts Management
- Add new contacts with name, address, phone number, email, and birthday
- Search contacts by various criteria (e.g., name)
- Edit and delete existing contacts
- Show contacts with upcoming birthdays within a specified number of days
- Validate phone numbers and emails on input

### 🗒️ Notes Management
- Add, edit, and delete textual notes
- Search notes by content
- Add **tags** to categorize notes
- Search and sort notes by tags

### 🧠 Intelligent Features
- Smart analysis of user input to suggest the most relevant command
- Persistent data storage: all data (contacts and notes) are saved on disk and are available after restart

---

## 💻 Tech Stack

- **Language**: 🐍 Python 3
- **Version Control**: Git, GitHub
- **Data Storage**: Local file system (e.g., JSON or pickle format)
- **Libraries**: `datetime`, `re`, `os`, `sys`, and others from Python standard library

---

## ⏳ Timeline

- **Start Date**: [07.04.2025]
- **End Date**: [14.07.2025]
- Project duration: [1] week

---

## 🗂️ Project Structure

```
OUR_FINAL_PROJECT/
├── main.py               # Core logic of the assistant
├── classes_for_program.py # All classes used in the program (except Notes)
├── decor.py              # Decorator functions
├── functions_block.py    # All functions (except for notes)
├── note_class.py         # Class for Notes
├── note_functions.py     # Functions for managing notes
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation
```

---

## 🚀 How to Run

```bash
git clone https://github.com/AlexandrSergeevichKovalenko/OUR_FINAL_PROJECT.git
cd OUR_FINAL_PROJECT
python main.py
```

💡 **Tip:** You can also create a virtual environment and install dependencies from `requirements.txt` for best practice:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

# 🎯 Mission
To empower users with a smart and simple tool for managing personal information — contacts and notes — directly from the terminal.
Our goal is to combine clarity, efficiency, and ease of use in one powerful console assistant.

---

# 🌟 Vision
We envision a future where managing everyday information doesn’t require complex software.
Our assistant is the first step toward creating intelligent, accessible tools that simplify life — one command at a time.

---

# 📜 Licence

This project is a group work published under the [MIT license](https://github.com/AlexandrSergeevichKovalenko/OUR_FINAL_PROJECT/blob/2e866a8b284d8b8fae3073b025958b7f67ec8bb5/LICENSE.txt), and all project contributors are listed in the license text.

---

# 👏 Acknowledgments

This project was created by a passionate team as part of the final project for the [GoIT](https://goit.global/) **Python Core** course.
Special thanks to our mentors and classmates for their feedback and support throughout the development journey.
Thank you for exploring our work — we hope you enjoy using our Assistant!

---

### 📌 Final Note

> This assistant is our step toward creating a more organized and productive digital environment  
> using simple but powerful console tools.  
>  
> We hope it will become a helpful everyday companion ✨
