from tkinter import *
from tkinter import messagebox
from math import *
import os
import urllib.request
import ctypes

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

BG_COLOR = "#1f262b"
ACCENT_COLOR = "#4a90e2"
BTN_COLOR = "#4C4281"
TEXT_COLOR = "#f4f4f4"
FONT_MAIN = (font_family, 10)
FONT_BOLD = (font_family, 10, "bold")

root.title("Значення тригонометричних функцій")
root.iconbitmap(default="img/logo.ico")
root.geometry("480x250+500+100")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

top_frame = LabelFrame(
    root, text="Вхідні дані", bg=BG_COLOR, font=FONT_BOLD, fg=ACCENT_COLOR
)

label_1 = Label(
    top_frame,
    text="Укажіть градусну міру кута:",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
entry_1 = Entry(
    top_frame,
    width=7,
    font=FONT_MAIN,
    relief=FLAT,
    highlightthickness=5,
    highlightbackground=ACCENT_COLOR,
    highlightcolor=ACCENT_COLOR,
    borderwidth=0,
    background=ACCENT_COLOR,
    fg=TEXT_COLOR,
)
button_1 = Button(
    top_frame,
    text="Обчислити",
    width=20,
    bg=BTN_COLOR,
    fg="white",
    font=FONT_BOLD,
    cursor="hand2",
    relief=FLAT,
)

top_frame.pack(padx=10, pady=10, fill=BOTH)
label_1.pack(side=LEFT, padx=10, pady=20)
entry_1.pack(side=LEFT, padx=10, pady=20)
button_1.pack(side=LEFT, padx=10, pady=20)

bottom_frame = LabelFrame(
    root, text="Вихідні дані", bg=BG_COLOR, font=FONT_BOLD, fg=ACCENT_COLOR
)
bottom_left_frame = Frame(bottom_frame, bg=BG_COLOR)
bottom_middle_frame = Frame(bottom_frame, bg=BG_COLOR)
bottom_right_frame = Frame(bottom_frame, bg=BG_COLOR)

answer_deg_rad = Label(bottom_left_frame, bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)
answer_sin = Label(bottom_middle_frame, bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)
answer_cos = Label(bottom_middle_frame, bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)
answer_tan = Label(bottom_right_frame, bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)
answer_ctan = Label(bottom_right_frame, bg=BG_COLOR, font=FONT_MAIN, fg=TEXT_COLOR)

bottom_frame.pack(padx=10, pady=5, fill=BOTH)
bottom_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
bottom_middle_frame.pack(side=LEFT, fill=BOTH, expand=True)
bottom_right_frame.pack(side=LEFT, fill=BOTH, expand=True)


answer_deg_rad.pack(anchor=CENTER, pady=10)
answer_sin.pack(anchor=CENTER, pady=5)
answer_cos.pack(anchor=CENTER, pady=5)
answer_tan.pack(anchor=CENTER, pady=5)
answer_ctan.pack(anchor=CENTER, pady=5)

author = Label(
    root,
    text="\u00a9 Шарандак О.В, ПЗ-25-1",
    bg=BG_COLOR,
    font=(font_family, 8, "italic"),
    fg="#888888",
)
author.pack(side=BOTTOM, padx=10, pady=10)


def calculate(event=None):
    try:
        alpha_deg = float(entry_1.get())
        alpha_rad = radians(alpha_deg)
        sin_alpha = sin(alpha_rad)
        cos_alpha = cos(alpha_rad)

        if abs(cos_alpha) < 1e-10:
            tan_res = "не визн."
        else:
            tan_res = f"{tan(alpha_rad):.3f}"

        if abs(sin_alpha) < 1e-10:
            ctan_res = "не визн."
        else:
            ctan_res = f"{1 / tan(alpha_rad):.3f}"

        answer_deg_rad["text"] = f"{alpha_deg:.4g}° = {alpha_rad:.4g} рад"
        answer_sin["text"] = f"sin: {sin_alpha:.3f}"
        answer_cos["text"] = f"cos: {cos_alpha:.3f}"
        answer_tan["text"] = f"tan: {tan_res}"
        answer_ctan["text"] = f"ctan: {ctan_res}"

    except ValueError:
        answer_deg_rad["text"] = "Помилка вводу!"
        answer_sin["text"] = ""
        answer_cos["text"] = ""
        answer_tan["text"] = ""
        answer_ctan["text"] = ""


button_1.bind("<Button-1>", calculate)
entry_1.bind("<Return>", calculate)

root.mainloop()
