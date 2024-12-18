import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget)

"""
Layout diagram:
     ____________________________
    | Guess label                |
    +-------------+--------------+
    | Guess entry | Guess button |
    +-------------+--------------+
    | Scrollable output label    |
    |____________________________|

"""

class GuessingGame():
    def __init__(self):
        # Set up the app
        app = QApplication([])

        # Window and base widget
        window = QMainWindow()
        window.setWindowTitle("Guessing Game")
        base = QWidget(window)
        window.setCentralWidget(base)

        # Outer vertical layout
        vbox = QVBoxLayout(base)

        # Guess label
        self.guessLabel = QLabel(base)
        vbox.addWidget(self.guessLabel)

        # Horizontal layout holding guess entry and button
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        self.guessEntry = QLineEdit(base)
        hbox.addWidget(self.guessEntry)

        self.guessButton = QPushButton(base)
        self.guessButton.setText("Guess")
        hbox.addWidget(self.guessButton)

        # Scroll area holding output label
        scrollArea = QScrollArea(base)
        scrollArea.setWidgetResizable(True)
        self.outputLabel = QLabel(scrollArea)
        self.outputLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        scrollArea.setWidget(self.outputLabel)

        vbox.addWidget(scrollArea)

        # Initialize the game state
        self.start_game()

        # Show the window built above
        window.resize(400, 300)
        window.show()

        # Exit when the app exits
        sys.exit(app.exec())
    
    def start_game(self):
        self.guessLabel.setText("[guessLabel]")
        self.outputLabel.setText("[outputLabel]")

if __name__ == "__main__":
    # # For screen share demonstration, scale up the entire app
    # import os
    # os.environ["QT_SCALE_FACTOR"] = "3"
    GuessingGame()