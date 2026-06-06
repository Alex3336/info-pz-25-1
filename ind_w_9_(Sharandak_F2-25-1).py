import ctypes
import os
import random
import string
import urllib.request
import pyperclip
from tkinter import *
from tkinter import messagebox, ttk

font_url = "https://github.com/google/fonts/raw/main/ufl/ubuntu/Ubuntu-Regular.ttf"
font_filename = "Ubuntu-Regular.ttf"

root = Tk()
root.withdraw()

if not os.path.exists(font_filename):
    if messagebox.askyesno(
        "Завантаження шрифту",
        "Шрифт 'Ubuntu' не знайдено. Бажаєте завантажити його для кращого вигляду програми?",
    ):
        try:
            print("Завантаження шрифту Ubuntu...")
            urllib.request.urlretrieve(font_url, font_filename)
            print("Завантаження завершено.")
        except Exception as e:
            print(f"Помилка завантаження шрифту: {e}")
    else:
        print(
            "Користувач відмовився від завантаження. Використовується системний шрифт."
        )

if os.name == "nt" and os.path.exists(font_filename):
    ctypes.windll.gdi32.AddFontResourceExW(font_filename, 0x10, 0)
    myappid = "mycompany.myproduct.subproduct.version"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root.deiconify()

font_family = "Ubuntu" if os.path.exists(font_filename) else "Arial"


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


BG_COLOR = "#1f262b"
ACCENT_COLOR = "#4a90e2"
BTN_COLOR = "#4C4281"
TEXT_COLOR = "#f4f4f4"
FONT_MAIN = (font_family, 10)
FONT_BOLD = (font_family, 10, "bold")


root.title("Генерація пароля")
root.iconbitmap(default="img/logo_2.ico")
center_window(root, 510, 185)
root.resizable(False, False)
root.configure(bg=BG_COLOR)


style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Password.TCombobox",
    fieldbackground=ACCENT_COLOR,
    background=ACCENT_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    bordercolor=ACCENT_COLOR,
    lightcolor=ACCENT_COLOR,
    darkcolor=ACCENT_COLOR,
    font=FONT_MAIN,
)
style.map(
    "Password.TCombobox",
    fieldbackground=[("readonly", ACCENT_COLOR)],
    foreground=[("readonly", TEXT_COLOR)],
)
style.configure(
    "Password.TCheckbutton",
    background=BG_COLOR,
    foreground=TEXT_COLOR,
    font=FONT_MAIN,
)
style.map(
    "Password.TCheckbutton",
    background=[("active", BG_COLOR)],
    foreground=[("active", ACCENT_COLOR), ("selected", ACCENT_COLOR)],
)


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Помилка", "Довжина пароля повинна бути цілим числом.")
        return

    if length <= 0:
        messagebox.showerror("Помилка", "Довжина пароля повинна бути більшою за 0.")
        return

    characters = ""

    if digits_var.get():
        characters += string.digits
    if letters_var.get():
        characters += string.ascii_letters
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Помилка", "Оберіть хоча б один тип символів.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    messagebox.showinfo("Згенерований пароль", f"Ваш пароль: \n{password}\tскопійовано до буферу обміну.")
    pyperclip.copy(password)


input_data = LabelFrame(
    root,
    text="Вхідні дані:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
input_data.place(x=10, y=10, width=490, height=135)

length_label = Label(
    input_data,
    text="Довжина пароля:",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)
length_label.grid(row=0, column=0, padx=(5, 3), pady=8, sticky=W)

length_entry = ttk.Entry(
    input_data,
    width=45,
    font=FONT_MAIN,
    justify=LEFT,
)
length_entry.grid(row=0, column=1, padx=3, pady=8, columnspan=3)

type_label = Label(
    input_data,
    text="Тип символів:",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)
type_label.grid(row=1, column=0, padx=(5, 3), pady=8, sticky=W)

digits_var = BooleanVar(value=True)
letters_var = BooleanVar(value=False)
symbols_var = BooleanVar(value=False)

digits_check = ttk.Checkbutton(
    input_data,
    text="Цифри",
    variable=digits_var,
    style="Password.TCheckbutton",
)
digits_check.grid(row=1, column=1, pady=2, sticky=W)

letters_check = ttk.Checkbutton(
    input_data,
    text="Літери",
    variable=letters_var,
    style="Password.TCheckbutton",
)
letters_check.grid(row=1, column=2, pady=2, sticky=W)

symbols_check = ttk.Checkbutton(
    input_data,
    text="Символи",
    variable=symbols_var,
    style="Password.TCheckbutton",
)
symbols_check.grid(row=1, column=3, pady=2, sticky=W)

generate_button = Button(
    input_data,
    text="Згенерувати",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    cursor="hand2",
    width=16,
    command=generate_password,
)
generate_button.place(relx=0.5, y=90, anchor=CENTER)

author = Label(
    root,
    text="\u00a9 Шарандак О.В., ПЗ-25-1",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=(font_family, 8, "italic"),
)
author.place(relx=0.5, y=165, anchor=CENTER)

root.mainloop()
