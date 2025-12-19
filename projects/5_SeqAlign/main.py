from gui.menu import App
import tkinter as tk
import os

SRC_FOLDER = os.path.dirname(os.path.realpath(__file__)) # Pasta mãe

OUTPUT_PATH = os.path.join(SRC_FOLDER, 'output.txt')
ICON1_PATH = os.path.join(SRC_FOLDER, 'docs/assets/icons/menu.png')
ICON2_PATH = os.path.join(SRC_FOLDER, 'docs/assets/icons/help.png')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root, OUTPUT_PATH, ICON1_PATH, ICON2_PATH)
    root.mainloop()