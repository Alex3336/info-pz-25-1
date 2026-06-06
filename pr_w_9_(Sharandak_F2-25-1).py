from calendar import monthrange
from datetime import date
from tkinter import *
from tkinter import messagebox, ttk
import ctypes
import os
import urllib.request

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
ERROR_COLOR = "#ff6b6b"
FONT_MAIN = (font_family, 10)
FONT_BOLD = (font_family, 10, "bold")
FONT_SMALL = (font_family, 8)

MONTHS = [
    "січень",
    "лютий",
    "березень",
    "квітень",
    "травень",
    "червень",
    "липень",
    "серпень",
    "вересень",
    "жовтень",
    "листопад",
    "грудень",
]


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def get_birth_date():
    day = int(day_combo.get())
    month = get_selected_month()
    year = int(year_combo.get())
    return date(year, month, day)


def get_selected_month():
    return MONTHS.index(month_combo.get()) + 1


def update_day_combo(event=None):
    if not month_combo.get() or not year_combo.get():
        return

    selected_day = day_combo.get()
    year = int(year_combo.get())
    month = get_selected_month()
    days_count = monthrange(year, month)[1]
    day_values = [str(day) for day in range(1, days_count + 1)]

    day_combo.config(values=day_values)

    if selected_day and int(selected_day) <= days_count:
        day_combo.set(selected_day)
    else:
        day_combo.set(str(days_count))


def reset_date_combos():
    today = date.today()
    month_combo.current(today.month - 1)
    year_combo.set(str(today.year - 18))
    update_day_combo()
    days_count = monthrange(int(year_combo.get()), get_selected_month())[1]
    day_combo.current(min(today.day, days_count) - 1)


def capitalize_entry(entry):
    value = entry.get().strip()

    if value:
        value = value[0].upper() + value[1:]
        entry.delete(0, END)
        entry.insert(0, value)

    return value


def focus_next_entry(current_entry, next_entry):
    capitalize_entry(current_entry)
    next_entry.focus_set()
    next_entry.icursor(END)
    return "break"


def finish_name_input():
    capitalize_entry(patronymic_entry)
    day_combo.focus_set()
    return "break"


def show_result():
    surname = capitalize_entry(surname_entry)
    name = capitalize_entry(name_entry)
    patronymic = capitalize_entry(patronymic_entry)

    if not surname or not name or not patronymic:
        messagebox.showwarning("Аналізатор повноліття", "Заповніть усі поля ПІБ.")
        return

    try:
        birthday = get_birth_date()
    except ValueError:
        messagebox.showerror("Аналізатор повноліття", "Вибраної дати не існує.")
        result_status.config(text="Некоректна дата", fg=ERROR_COLOR)
        return

    if birthday > date.today():
        messagebox.showerror(
            "Аналізатор повноліття", "Дата народження не може бути у майбутньому."
        )
        result_status.config(text="Некоректна дата", fg=ERROR_COLOR)
        return

    age = calculate_age(birthday)
    is_adult = age >= 18
    status = "Повнолітня людина" if is_adult else "Неповнолітня людина"
    status_color = ACCENT_COLOR if is_adult else ERROR_COLOR

    result_name.config(text=f"{surname} {name} {patronymic}")
    result_birth.config(text=f"дата народження: {birthday.strftime('%d.%m.%Y')}")
    result_age.config(text=f"повних років: {age}")
    result_status.config(text=status, fg=status_color)

    (
        messagebox.showinfo(
            "Аналізатор повноліття",
            f"{status},\nповних років: {age}",
        )
        if status == "Повнолітня людина"
        else messagebox.showerror(
            "Аналізатор повноліття",
            f"{status},\nповних років: {age}",
        )
    )
    reset_date_combos()


def clear_form():
    surname_entry.delete(0, END)
    name_entry.delete(0, END)
    patronymic_entry.delete(0, END)
    reset_date_combos()
    result_name.config(text="---")
    result_birth.config(text="дата народження: ---")
    result_age.config(text="повних років: ---")
    result_status.config(text="Очікує обробки", fg=ACCENT_COLOR)
    surname_entry.focus_set()


root.title("Аналізатор повноліття")
center_window(root, 510, 460)
root.resizable(False, False)
root.configure(bg=BG_COLOR)

icon_path = os.path.join("img", "logo_2.ico")
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TCombobox",
    fieldbackground=ACCENT_COLOR,
    background=ACCENT_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    bordercolor=ACCENT_COLOR,
    lightcolor=ACCENT_COLOR,
    darkcolor=ACCENT_COLOR,
    focuscolor=ACCENT_COLOR,
    borderwidth=0,
    relief=FLAT,
    padding=1,
)
style.map(
    "TCombobox",
    fieldbackground=[("readonly", ACCENT_COLOR)],
    bordercolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
    lightcolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
    darkcolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
)

person_frame = LabelFrame(
    root,
    text="Вкажіть прізвище ім'я по батькові:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
person_frame.place(x=20, y=20, width=470, height=140)

field_labels = ("прізвище", "ім'я", "по батькові")
entries = []

for row, text in enumerate(field_labels):
    label = Label(person_frame, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN)
    label.grid(row=row, column=0, padx=(16, 8), pady=8, sticky=W)

    entry = Entry(
        person_frame,
        width=20,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief=FLAT,
        font=FONT_MAIN,
    )
    entry.grid(row=row, column=1, padx=8, pady=8, sticky=W)
    entries.append(entry)

surname_entry, name_entry, patronymic_entry = entries

surname_entry.bind("<Return>", lambda event: focus_next_entry(surname_entry, name_entry))
surname_entry.bind("<KP_Enter>", lambda event: focus_next_entry(surname_entry, name_entry))
surname_entry.bind("<Tab>", lambda event: focus_next_entry(surname_entry, name_entry))
name_entry.bind("<Return>", lambda event: focus_next_entry(name_entry, patronymic_entry))
name_entry.bind("<KP_Enter>", lambda event: focus_next_entry(name_entry, patronymic_entry))
name_entry.bind("<Tab>", lambda event: focus_next_entry(name_entry, patronymic_entry))
patronymic_entry.bind("<Return>", lambda event: finish_name_input())
patronymic_entry.bind("<KP_Enter>", lambda event: finish_name_input())
patronymic_entry.bind("<Tab>", lambda event: finish_name_input())

date_frame = LabelFrame(
    root,
    text="Вкажіть день, місяць, рік народження:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
date_frame.place(x=20, y=165, width=470, height=130)

date_labels = ("дата", "місяць", "рік")
for row, text in enumerate(date_labels):
    label = Label(date_frame, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN)
    label.grid(row=row, column=0, padx=(16, 8), pady=6, sticky=W)

today = date.today()
days = [str(day) for day in range(1, 32)]
years = [str(year) for year in range(today.year, 1900, -1)]

day_combo = ttk.Combobox(
    date_frame, values=days, width=12, state="readonly", font=FONT_MAIN
)
month_combo = ttk.Combobox(
    date_frame, values=MONTHS, width=12, state="readonly", font=FONT_MAIN
)
year_combo = ttk.Combobox(
    date_frame, values=years, width=12, state="readonly", font=FONT_MAIN
)

day_combo.grid(row=0, column=1, padx=8, pady=6, sticky=W)
month_combo.grid(row=1, column=1, padx=8, pady=6, sticky=W)
year_combo.grid(row=2, column=1, padx=8, pady=6, sticky=W)

month_combo.bind("<<ComboboxSelected>>", update_day_combo)
year_combo.bind("<<ComboboxSelected>>", update_day_combo)

reset_date_combos()

process_button = Button(
    root,
    text="Обробити дані",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    width=18,
    cursor="hand2",
    command=show_result,
)
process_button.place(x=100, y=305, height=30)

clear_button = Button(
    root,
    text="Очистити",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    width=12,
    cursor="hand2",
    command=clear_form,
)
clear_button.place(x=290, y=305, height=30)

result_frame = LabelFrame(
    root,
    text="Опрацьовані дані особи:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
result_frame.place(x=20, y=340, width=470, height=80)

result_name = Label(
    result_frame, text="---", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN
)
result_birth = Label(
    result_frame,
    text="дата народження: ---",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)
result_age = Label(
    result_frame, text="повних років: ---", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN
)
result_status = Label(
    result_frame, text="Очікує обробки", bg=BG_COLOR, fg=ACCENT_COLOR, font=FONT_MAIN
)

result_name.grid(row=0, column=0, padx=(12, 25), pady=(4, 0), sticky=W)
result_status.grid(row=0, column=1, padx=5, pady=(4, 0), sticky=W)
result_birth.grid(row=1, column=0, padx=(12, 25), sticky=W)
result_age.grid(row=1, column=1, padx=5, sticky=W)

author = Label(
    root,
    text="\u00a9 Шарандак О.В., ПЗ-25-1",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=(font_family, 8, "italic"),
)
author.place(x=20, y=425)

surname_entry.focus_set()
root.mainloop()
