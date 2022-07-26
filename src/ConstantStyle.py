from tkinter.constants import NORMAL, END

"""
This class is to unify the GUI style of this project.
"""

# Colors
BACKGROUND = "#696969"
SECONDARY = "#b5b5b5"
FILL_COLOR = "black"
BACK_COLOR = "white"

# Fonts
FONT_1 = ("Helvetica", 14)  # ("Century Gothic", 14, BOLD)
FONT_2 = ("Helvetica", 16)


# For Placeholder
def removePlaceholder(event, current_entry):
    current_entry.configure(state=NORMAL)
    current_entry.delete(0, END)


# Hovering
# def changeOnHover(button, colorOnHover, colorOnLeave):
#     button.bind("<Enter>", func=lambda e: button.config(
#         background=colorOnHover))
#
#     button.bind("<Leave>", func=lambda e: button.config(
#         background=colorOnLeave))


def get_entry_text(entry, placeholder_text):
    input = entry.get()
    input = input.strip()

    if input == "" or input == placeholder_text:
        input = None

    return input
