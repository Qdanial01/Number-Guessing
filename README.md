# Number Guessing Game
There are 2 python files in this project both of which serve the purpose of a number Guessing Game
- Number_Guess_Game.py (**Command Line Version**) - Basic version of a number guessing game written in Python.
- Number_Guess_Game_with_GUI.py (**Integrated GUI**) - UI built into the game with TKinter

GUI version contains a standalone **Windows executable(.exe)**!

## **Command Line Version**
Number guessing game where players enter guesses in the terminal and receive feedback until they successfully guess the correct number.

### **Features:**
- Random number generation between 1 and 10
- Up to 10 attempts to guess the number
- Feedback on whether the guess is too high or too low
- Hint provided on the second-to-last attempt

### **How to Run:**
```bash
python Number_Guess_Game.py
```
---

## **GUI Version**
A graphical version of the number guessing game using Tkinter, featuring a user-friendly interface with buttons and messages.


### **Features:**
- Same gameplay as the command-line version
- Graphical input field instead of terminal-based input
- Error handling and message pop-ups for incorrect inputs
- Reset button to start a new game easily

## Running the EXE (No Python Required)
Option 1 (Through zip file)
1. Download the ZIP file from the **Releases** section.
2. Extract the ZIP file.
3. Open the extracted folder and double-click `Number_Guess_Game_with_gui.exe`.

Option 2 (Through dist/ folder)
1. Clone/download repository
2. Navigate dist/ folder
3. Run Number_Guess_Game_with_gui

### **How to Run:**
```bash
python Number_Guess_Game_with_gui.py
NumberGuesser/
```

## Project Structure
NumberGuesser/
│── build/ # Build files (can be ignored) 
│── dist/ # Contains the .exe file 
│── Number_Guess_Game.py # Command-line version 
│── Number_Guess_Game_with_gui.py # GUI version 
│── Number_Guess_Game_with_gui.spec # Spec file for PyInstaller 
│── README.md # Documentation 
│── Number_Guess_Game_with_gui.zip #Game packed into an executable file

## Building the exe on your own
If you wish to build the exe from the code itself, you can run this command in the terminal
Prerequisite:
1. Ensure pyinstaller is installed

```bash
pyinstaller --onefile --windowed Number_Guess_Game_with_gui.py
```

### **Clone the Repository:**
```bash
git clone https://github.com/Qdanial01/Number-Guessing.git
cd number-guesser
